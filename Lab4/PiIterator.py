from Fraction import *
from decimal import *

pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")
iterations = 1000000


class NilakanthaPiGenerator:
    @classmethod
    def NilakanthaPiGenerator(cls):
        fraction = Fraction(numerator=3, denominator=1)
        num = 2
        add_next = True
        while True:
            denominator = num * (num + 1) * (num + 2)
            next_value = Fraction(numerator=4, denominator=denominator)

            if add_next:
                fraction = fraction + next_value
                add_next = False

            else:
                fraction = fraction - next_value
                add_next = True
            num = num + 2
            yield fraction.value


class LeibnizPiIterator:
    def __init__(self):
        pass
        # For this method, simply use a pass command.  All of the setup will occur in __iter__

    def __iter__(self):
        self.fraction = Fraction(numerator=0, denominator=1)
        self.n = 1
        self.add_next = True
        return self

        # o This method initializes the values we will need for the iterator
        # o Create an instance variable called self.fraction and assign to it a Fraction object with a
        # numerator of 0 and denominator of 1.  This will represent the running total for the
        # series.
        # o Create an instance variable called self.n and assign 1 to it.  This will represent the
        # denominator to be used in the next iteration (see documentation above).
        # o Create an instance variable called self.add_next and assign to it True.  This is a Boolean
        # value indicating if the next iteration will be an add or subtract.
        # o Return self

    def __next__(self):
        next_value = Fraction(numerator=4, denominator=self.n)
        if self.add_next:
            self.fraction = self.fraction + next_value
            self.add_next = False

        else:
            self.fraction = self.fraction - next_value
            self.add_next = True
        self.n += 2

        return self.fraction.value

        # o This method is where the work is done for each iteration.
        # o If self.add_next is True then the next value is to be added to self.fraction.  Otherwise,
        # subtract it.
        # o The next value is a new Fraction object with the value 4 / self.n
        # o After updating self.fraction do the following:
        # ▪ Change the value of self.add_next to its opposite.
        # ▪ Add 2 to self.n
        # ▪ Return self.fraction.value
