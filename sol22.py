# list all students
import sqlite3

# create table if not already exists
conn = sqlite3.connect("data.db")
conn.execute('''
CREATE TABLE IF NOT EXISTS student(
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    age INT
);
''')

# list all students
cursor = conn.execute('''
SELECT rowid , name , city ,age  FROM STUDENT;
''')

for row in cursor:
    print("{0} , {1} , {2} , {3}".format(row[0], row[1], row[2], row[3]))

conn.close()
