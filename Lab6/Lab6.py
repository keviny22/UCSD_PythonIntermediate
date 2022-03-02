import multiprocessing
from threading import Semaphore, Thread, Lock
from queue import Queue, Empty
from random import randint
from time import sleep
from logging import basicConfig, debug, DEBUG

basicConfig(level=DEBUG, format='[%(threadName)-9s] %(message)s')

max_customers_in_bank = 3  # maximum number of customers that can be in the bank at one time
max_customers = 7  # number of customers that will go to the bank today
max_tellers = 2  # number of tellers working today
teller_timeout = 10  # longest time that a teller will wait for new customers


class Customer:
    def __init__(self, name):
        """
        This method accepts a name string and will assign it to self.name
        :param name:
        """
        self.name = name

    def __str__(self):
        """
        This method will output a string in the following format: “{self.name}”
        :return:
        """
        return self.name


class Teller:
    def __init__(self, name):
        """
        This method accepts a name string and will assign it to self.name
        :param name:
        """
        self.name = name

    def __str__(self):
        """
        This method will output a string in the following format: “{self.name}”
        :return:
        """
        return self.name


def bankprint(lock, msg):
    """
    The bankprint() function will be where all print commands are sent.  It has the following signature:
    :param lock: Lock object that must be acquired before the print() function is called.
    Hint: Use a with context manager block on the lock object
    :param msg: text to print
    :return:
    """

    lock.acquire()
    try:
        debug(msg)
    finally:
        lock.release()


# Tellers to service customer
def teller_job(teller: Teller, guard: Semaphore, teller_line: Queue, printlock: Lock):
    bankprint(printlock, f"[T] Teller {teller} has started work.")

    while True:
        try:
            customer = teller_line.get(timeout=teller_timeout)
            bankprint(printlock, f"[T] Teller {t.name} is now helping a customer {customer.name}")
            sleep(randint(1, 4))
            bankprint(printlock, f"[T] Teller {t.name} has finished helping customer {customer.name}")
            bankprint(printlock, f"<G> Guard is letting customer {customer.name} out of the bank")
            guard.release()
        except Empty:
            bankprint(printlock, f"[T] Teller {teller.name} is going on break")
            break


# Thread function
def wait_outside_bank(customer: Customer, guard: Semaphore, teller_line: Queue, printlock: Lock):
    """
    A thread function
    # Print a customer message indicating that the customer is waiting outside the bank
    # Attempt to acquire a semaphore from the guard object (do NOT use a context manager here
    #   since the semaphore is to be released in another method)
    # Print a security guard message indicating they have let that customer into the bank
    # Print a customer message indicating they are trying to get into line
    # Put the customer into the teller_line queue (queue’s put() method)
    :param customer: Customer object
    :param guard: secuirty guard Semiphore
    :param teller_line: the Queue
    :param printlock: is the Lock
    :return:
    """
    bankprint(printlock, f"(C) Customer {customer} is waiting outside the bank.")

    guard.acquire()

    bankprint(printlock, f"<G> Guard has let customer: {customer} has been let inside the bank.")
    bankprint(printlock, f"(C) Customer {customer} is trying to get into line.")

    teller_line.put(customer, timeout=teller_timeout)

    bankprint(printlock, f"(C) Customer {customer} is in line.")


if __name__ == '__main__':

    # printlock Lock object which will be passed to all of the thread functions and used by bankprint():
    printlock = Lock()
    multiprocessing.set_start_method = "fork"

    # a Queue called teller_line which represents the line customers get into waiting for a teller
    # (the maxsize parameter need to be set to the max_customers_in_bank value):
    teller_line = Queue(maxsize=max_customers_in_bank)

    # Semaphore object that represents a security guard
    guard = Semaphore(max_customers_in_bank)

    bankprint(printlock, "<G> Security guard starting their shift")
    bankprint(printlock, "*B* Bank open")
    bankprint(printlock, f"*B* We have {max_customers} coming to the bank today")
    bankprint(printlock, f"*B* We have {max_tellers} tellers working today")
    bankprint(printlock, f"*B* The guard has been instructed to allow {max_customers_in_bank} in the bank at a time")

    customers = []
    for i in range(1, max_customers + 1):
        c = Thread(name=f"Customer {i}", target=wait_outside_bank,
                   args=(Customer(f"customer_{i}"), guard, teller_line, printlock))
        c.start()
        customers.append(c)

    sleep(5)
    bankprint(printlock, f"*B* {max_tellers} tellers are starting work....")
    tellers = []
    for i in range(1, max_tellers + 1):
        t = Thread(name=f"Teller {i}", target=teller_job, args=(Teller(f"teller_{i}"), guard, teller_line, printlock))
        t.start()
        tellers.append(t)

    for customer in customers:
        customer.join()

    for teller in tellers:
        teller.join()

    bankprint(printlock, "*B* Bank is closed")
