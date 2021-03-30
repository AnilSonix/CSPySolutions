# update student
import sqlite3

rowid = input("Enter id to update : ")
name = input("Enter new name : ")
city = input("Enter new city : ")
age = input("Enter new age : ")

# create table if not already exists
conn = sqlite3.connect("data.db")
conn.execute('''
CREATE TABLE IF NOT EXISTS student(
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    age INT
);
''')

# delete student with id
conn.execute('''
UPDATE  STUDENT SET NAME = "{0}" , CITY = "{1}" , AGE= {2} WHERE ROWID = {3};
'''.format(name, city, age, rowid))

conn.commit()
print("Row affected  : {0} ".format(conn.total_changes))

# list all students
cursor = conn.execute('''
SELECT rowid , name , city ,age  FROM STUDENT;
''')

for row in cursor:
    print("{0} , {1} , {2} , {3}".format(row[0], row[1], row[2], row[3]))

conn.close()
