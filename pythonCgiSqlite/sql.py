#!/usr/bin/env python
import cgi
import sqlite3

form = cgi.FieldStorage()

fname = form.getvalue('firstName')
lname = form.getvalue('lastName')
course = form.getvalue('course')
workType = form.getvalue('workType')
grades = form.getvalue('grades')

def convert(grades):
   glst=list(grades.split(","))
   return glst

def grade(lst):
   total = 0
   for g in lst:
      g=int(g)
      total+=g
   avg = total/len(lst)

   if avg>80:
      grade='A'
   elif avg>=70 and avg<79:
      grade='B'
   elif avg>=60 and avg<69:
      grade='C'
   elif avg>=50 and avg<59:
      grade='D'
   else:
      grade="F"
   return grade

glst=convert(grades)
grade=grade(glst) 

def course_name(course):
   if course==1:
      courseName="CST8260-database"
   elif course==2:
      courseName="CST8209-javascript"
   elif course==3:
      courseName="CST8279-python"
   else:
      courseName="MAD9013-html/css"
   return courseName

courseName=course_name(course)

def workType_name(workType):
   if workType==1:
      workTypeName="Assignments"
   elif workType==2:
      workTypeName="Midterms"
   else:
      workTypeName="Final Exam"
   return workTypeName

workTypeName=workType_name(workType)

print "Content-type:text/html\r\n\r\n"

print "<html>"
print "<head>"
print "</head>"
print "<body>"
print "<p><b>Name:  %s %s</b></p>"%(fname,lname)
print "<p><b>Course:  %s</b></p>"%courseName
print "<p><b>Work Type:  %s</b></p>"%workTypeName
print "<p><b>Grade:  %s</b></p>"%grade
print "</body></html>"

conn = sqlite3.connect('gradeSystem.db')
cur = conn.cursor()

cur.execute('INSERT INTO Students(first_name,last_name) VALUES(?, ?)',(fname, lname))

cur.execute('INSERT INTO Grade(course_id,workType_id,grade) VALUES(?,?,?)',(course,workType,grade))

conn.commit()







