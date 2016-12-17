#!/usr/bin/env python
import cgi
import sqlite3

conn = sqlite3.connect('gradeSystem.db')
cur = conn.cursor()

cur.execute('SELECT Students.first_name,Students.last_name, Course.name,WorkType.name,Grade.grade FROM Students INNER JOIN Course ON Students.Id=Grade.Id INNER JOIN Grade ON Grade.course_id=Course.Id INNER JOIN WorkType ON WorkType.Id=Grade.workType_id ')
data= cur.fetchall()

print "Content-type:text/html\r\n\r\n"

print "<html>"
print "<head>"
print "</head>"
print "<body>"
print "<table class='table'>"
print "<thead>"
print "<th class='warning'>First Name</th>"
print "<th class='warning'>Last Name</th>"
print "<th class='warning'>Course</th>"
print "<th class='warning'>Work Type</th>"
print "<th class='warning'>Grade</th>"
print "</thead>"
print "<tbody>"
for row in data:
   print "<tr class='active'>"
   for d in row:
      print "<td>%s</td>"%d
   print "</tr>"
print "</tbody>"
print "</table>"
print "</body></html>"





