# add new student
import sqlite3

name = input("Enter name : ")
city = input("Enter city : ")
age = input("Enter age : ")

# create table if not already exists
conn = sqlite3.connect("data.db")
conn.execute('''
CREATE TABLE IF NOT EXISTS student(
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    age INT
);
''')

# write all details to it
conn.execute('''
INSERT INTO STUDENT ( NAME,CITY,AGE)
VALUES ("{0}","{1}","{2}");
'''.format(name, city, age))


conn.commit()
conn.close()
