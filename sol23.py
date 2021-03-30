# delete existing student
import sqlite3

rowid = input("Enter id to remove : ")

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
DELETE  FROM STUDENT WHERE ROWID = {0}
'''.format(rowid))

conn.commit()
print("Row affected  : {0} ".format(conn.total_changes))

# list all students
cursor = conn.execute('''
SELECT rowid , name , city ,age  FROM STUDENT;
''')

for row in cursor:
    print("{0} , {1} , {2} , {3}".format(row[0], row[1], row[2], row[3]))

conn.close()
