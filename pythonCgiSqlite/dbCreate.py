#!/usr/bin/env python
import sqlite3
import cgi

db_name = "gradeSystem.db"
conn = sqlite3.connect(db_name)
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS Students;')
student_table="CREATE TABLE Students(Id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT, last_name TEXT,FOREIGN KEY(Id) REFERENCES Grade(Id))"

cur.execute(student_table)
print "table created"

conn.execute('DROP TABLE IF EXISTS Course;')
course_table="CREATE TABLE Course(Id INTEGER PRIMARY KEY,name TEXT)"

cur.execute(course_table)
cur.execute('INSERT INTO Course VALUES(?,?)', (1,"database"))
cur.execute('INSERT INTO Course VALUES(?,?)', (2,"javascript",))
cur.execute('INSERT INTO Course VALUES(?,?)', (3,"python",))
cur.execute('INSERT INTO Course VALUES(?,?)', (4,"html/css",))
print "table created"

conn.execute('DROP TABLE IF EXISTS WorkType;')
workType_table="CREATE TABLE WorkType(Id INTEGER PRIMARY KEY,name TEXT)"

cur.execute(workType_table)
cur.execute('INSERT INTO WorkType VALUES(?,?)', (1,"assignment",))
cur.execute('INSERT INTO WorkType VALUES(?,?)', (2,"midterms",))
cur.execute('INSERT INTO WorkType VALUES(?,?)', (3,"finalExam",))
print "table created"

conn.execute('DROP TABLE IF EXISTS Grade;')
grade_table="CREATE TABLE Grade(Id INTEGER PRIMARY KEY AUTOINCREMENT, course_id INTEGER,workType_id INTEGER,grade TEXT, FOREIGN KEY(course_id) REFERENCES Course(Id),FOREIGN KEY(workType_id) REFERENCES WorkType(Id))"

cur.execute(grade_table)
print "table created" 
conn.commit()

