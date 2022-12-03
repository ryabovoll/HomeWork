import sqlite3
from faker import Faker
from random import randint

faker = Faker()
db = 'lc3.db'


def create_tb_person():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS person(
    person_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    Address VARCHAR(1024) NOT NULL, 
    job VARCHAR(128) NOT NULL, 
    Age INTEGER NOT NULL
    )
    '''
    cur.execute(sql)
    con.close()


def ins_data():
    create_tb_person()
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = f'''   
     INSERT INTO person (first_name, last_name, Address, job, Age)
     VALUES       
     ("{faker.first_name()}", "{faker.last_name()}", "{faker.address()}", "{faker.job()}", {randint(18, 60)})      
    '''
    cur.execute(sql)
    con.commit()
    con.close()


def drop_person():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = 'DROP TABLE IF EXISTS person'
    cur.execute(sql)
    con.close()


def prn_person():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''   
     SELECT * FROM person
    '''
    for row in cur.execute(sql):
        print(row)
    con.close()


def update_person():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''   
    UPDATE person
    SET  Age = 21
    WHERE person_id = 1
    '''
    cur.execute(sql)
    con.commit()
    con.close()


def del_person():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = "DELETE FROM person WHERE person_id = 11"
    cur.execute(sql)
    con.commit()
    con.close()


if __name__ == '__main__':
    # ins_data()
    # drop_person()
    # update_person()
    # del_person()
    prn_person()
