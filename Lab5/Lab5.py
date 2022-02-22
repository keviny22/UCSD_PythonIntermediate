import random
import sqlite3
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

people_db_file = "sqlite.db"  # The name of the database file to use
max_people = 500  # Number of records to create


def create_people_database(db_file, count):
    """
    :param db_file: db filename
    :param count: number of records to generate
    :return:
    """
    conn = sqlite3.connect(db_file)
    with conn:
        sql_create_people_table = """ CREATE TABLE IF NOT EXISTS people (
        id integer PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL); """
        cursor = conn.cursor()
        cursor.execute(sql_create_people_table)
        sql_truncate_people = "DELETE FROM people;"
        cursor.execute(sql_truncate_people)
        people = generate_people(count)
        sql_insert_person = "INSERT INTO people(id,first_name,last_name) VALUES(?,?,?);"
        for person in people:
            # print(person) # uncomment if you want to see the person object
            cursor.execute(sql_insert_person, person)
            # print(cursor.lastrowid) # uncomment if you want to see the row id
        cursor.close()


def generate_people(count):
    people = []
    with open('LastNames.txt', 'r') as lastfile:
        lastnames = [x.strip() for x in lastfile]

    with open('FirstNames.txt', 'r') as firstfile:
        firstnames = [x.strip() for x in firstfile]

    # change to compression
    for i in range(count):
        my_tuple = (
        i, firstnames[random.randint(0, len(firstnames) - 1)], lastnames[random.randint(0, len(lastnames) - 1)])
        people.append(my_tuple)

    return people


def test_PersonDB():
    with PersonDB(people_db_file) as db:
        print(db.load_person(10000))  # Should print the default
        print(db.load_person(122))
        print(db.load_person(300))


class PersonDB():
    def __init__(self, db_file=''):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

    def load_person(self, id):
        sql = "SELECT * FROM people WHERE id=?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        records = cursor.fetchall()
        result = (-1, '', '')  # id = -1, first_name = '', last_name = ''
        if records is not None and len(records) > 0:
            result = records[0]
        cursor.close()
        return result


def load_person(id, db_file):
    with PersonDB(db_file) as db:
        return db.load_person(id)


def load_database_multi_threaded(db_file, count):
    with ThreadPoolExecutor(10) as executor:
        future_list = [executor.submit(load_person, i, db_file) for i in range(count - 1)]
        for f in as_completed(future_list):
            print(f.result())


if __name__ == '__main__':
    people = generate_people(500)
    print(people)
    create_people_database(people_db_file, max_people)
    load_database_multi_threaded(people_db_file, max_people)
    test_PersonDB()


