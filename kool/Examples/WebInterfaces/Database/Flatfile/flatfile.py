#!/usr/bin/env python3

"""
An example demonstrating how to create a web interface to populate a flatfile
database using cherrypy and python3

This version in progress to match presentation setup

More information on cherrypy at:
http://docs.cherrypy.org/en/latest/tutorials.html

"""
import os, os.path
import string
import cherrypy
from cgi import parse_qs, escape

top = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<header>
<table style="width:100%">
  <tr>
  <th>
    <img src="/static/images/logo.png" alt="Kool Logo" style="height:128px;">
  </th>
  <th colspan="3">
  <h1>Kool</h1>
  </th>
  <th>
    <img src="/static/images/TartuLogo.png" alt="University of Tartu Logo" style="height:128px;">
  </th>
  </tr>
  </table>
</header>
<body>
"""

bottom = """
</body>
<footer>
<img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
</footer>
</html>
"""

startpage = """
<h2>Login</h2>
<form method="post" action="start">
  Email:<br> <input type="email" name="email"><br>
  Password:<br> <input type="password" name="pword"><br>
  <input type="radio" name="role" value="student" checked>Student
  <input type="radio" name="role" value="educator">Educator<br>
  <input type="submit" value="Submit">
</form>
"""

educator = """
<h2>Choose an option</h2>
<form method="post" action="educatoraction">
  <input type="radio" name="option" value="addstudent" checked>Add class member<br>
  <input type="radio" name="option" value="delstudent">Delete class member<br>
  <input type="radio" name="option" value="showstudentscore">Show class member grades<br>
  <input type="radio" name="option" value="makequiz">Make multiple choice quiz<br>
  <input type="submit" value="Submit">
</form>
"""

student = """
<h2>Choose an option</h2>
<form method="post" action="studentaction">
  <input type="radio" name="option" value="showmyscores">Show my scores<br>
  <input type="radio" name="option" value="takequiz">Take quiz<br>
  <input type="submit" value="Submit">
</form>
"""

addstudent = """
          <h2>Add student</h2>
            <form method="post" action="addstudentaction">
              <p>
                First name:<br>
                <input type="text" name="fname"><br>
                Last Name:<br>
                <input type="text" name="lname"><br>
                Email:<br>
                <input type="email" name="email"><br>
                Password:<br>
                <input type="password" name="pword1"><br>
                Repeat password:<br>
                <input type="password" name="pword2">
              </p>
              <p>
                 <input type="submit" value="Submit">
              </p>
            </form>
"""

showstudentscore = """
          <h2>Show student scores</h2>
            <form method="post" action="showstudentscoreaction">
              <p>
                Placeholder sliding menu for now<br>
                <select name="studenttodel" size="3">
                 <option value="orenge@ut.ee">Antony Orenge orenge@ut.ee</option>
                 <option value="benson.muite@ut.ee">Benson Muite benson.muite@ut.ee</option>
                 <option value="kira.lurich@ut.ee">Kira Lurich kira.lurich@ut.ee</option>
                </select>
                </p>
              <p>
                 <input type="submit" value="Submit selection">
              </p>
            </form>
"""

delstudent = """
          <h2>Select student record to delete from menu</h2>
            <form method="post" action="delstudentaction">
              <p>
              Placeholder sliding menu for now<br>
              <select name="studenttodel" size="3">
               <option value="orenge@ut.ee">Antony Orenge orenge@ut.ee</option>
               <option value="benson.muite@ut.ee">Benson Muite benson.muite@ut.ee</option>
               <option value="kira.lurich@ut.ee">Kira Lurich kira.lurich@ut.ee</option>
              </select>
                </p>
              <p>
                 <input type="submit" value="Submit selection">
              </p>
            </form>
"""

showmyscores = """
          <h2>My quiz scores</h2>
            <form method="post" action="returnstudentaction">
              <p>
                Placeholder for now - get scores from database and display them
                </p>
              <p>
                 <input type="submit" value="Return to student options">
              </p>
            </form>
"""

makequiz = """
          <h2>Make quiz</h2>
            <form method="post" action="makequizaction">
              <p>
                <p>
                  New quiz name:<br> <input type="text" name="qname"><br>
                  Number of questions (1-100):<br> <input type="number" name="numquestions"><br>
                  Multiple choice options per question (1-15):<br> <input type="number" name="numoptions"><br>
                  </p>
                </p>
              <p>
                 <input type="submit" value="Add questions">
              </p>
            </form>
"""

addquizquestion = """
          <h2>Add quiz question - modify to allow insertion of multiple questions</h2>
            <form method="post" action="addquizquestionaction">
              <p>
                  Question text:<br> <input type="text" name="qtext"><br>
                  option text:<br> <input type="text" name="otext0"><br>
                  option text:<br> <input type="text" name="otext1"><br>
                  Answer:<br> <input type="number" name="answer"><br>
                </p>
              <p>
                 <input type="submit" value="Add question">
              </p>
            </form>
"""

choosequiz = """
          <h2>Choose unattempted quiz to take</h2>
            <form method="post" action="choosequizaction">
              <p>
                Placeholder sliding menu for now<br>
                  <select name="quizchoice" size="5">
                   <option value="A">A</option>
                   <option value="B">B</option>
                   <option value="C">C</option>
                   <option value="D">D</option>
                   <option value="E">E</option>
                  </select>
                </p>
              <p>
                 <input type="submit" value="Submit">
              </p>
            </form>
"""

quiz = """
          <h2>Quiz</h2>
            <form method="post" action="gradequizaction">
              <p>
                Question 1<br>
                  <input type="radio" name="option" value="A">Answer 1<br>
                  <input type="radio" name="option" value="B">Answer 2<br>
                  <input type="radio" name="option" value="C">Answer 3<br>
                </p>
              <p>
                 <input type="submit" value="Submit">
              </p>
            </form>
"""

quizoptionstart = """
<form method="post" action="gradequizaction">
  <p>
"""

newquestion = """
<h3> Question text:<br> <input type="text" name="qtext"><br> </h3>
"""

quizoption = """
Option text:<br> <input type="text" name="otext">
<input type="radio" name="option" value="A">Correct answer<br>
"""
quizoptionend = """
  <input type="submit" value="Create quiz">
  </p>
</form>
"""

delstudentrecord = """
          <h2>Succefully deleted student record</h2>
            <form method="post" action="returneducatoraction">
                   <input type="submit" value="Return to educator options">
            </form>
"""

quizscore = """
          <h2>Quizscore</h2>
            <form method="post" action="quizscoreaction">
              <p>
                Placeholder, need to add question number<br>
                  Your answer to question 1 was right/wrong<br>
                </p>
              <p>
                 <input type="submit" value="Next question">
                 <input type="submit" value="Try again">
              </p>
            </form>
"""

class accessdatabase(object):
    @cherrypy.expose
    def index(self):
        page = top + startpage + bottom
        return page

    @cherrypy.expose
    def start(self,email,pword,role):
      # check password is correct one for supplied email address
        pwordemail='match'
        if ((pwordemail=='match') & (role=='educator')):
            page = top + educator + bottom
            return page
        elif ((pwordemail=='match') & (role=='student')):
            page = top + student + bottom
            return page
        else:
            page = top + startpage + bottom
            return page

    @cherrypy.expose
    def studentaction(self,option):
        if option=='showmyscores':
            page = top + showmyscores + bottom
            return page
        else:
            page = top + choosequiz + bottom
            return page

    @cherrypy.expose
    def educatoraction(self,option):
        if option=='addstudent':
            page = top + addstudent + bottom
            return page
        elif option=='delstudent':
            page = top + delstudent + bottom
            return page
        elif option=='makequiz':
            page = top + makequiz + bottom
            return page
        elif option=='showstudentscore':
            page = top + showstudentscore + bottom
            return page
        else:
            page = top + addstudentscore + bottom
            return page

    @cherrypy.expose
    def makequizaction(self,qname,numquestions,numoptions):
        quizoptions = quizoptionstart
        for nn in range(0, int(numquestions)):
            quizoptions = quizoptions + newquestion
            for n in range(0, int(numoptions)):
                quizoptions = quizoptions + quizoption
        quizoptions = quizoptions + quizoptionend

    #setup forms apporpriately to write to database
        page = top + quizoptions + bottom
        return page

    @cherrypy.expose
    def choosequizaction(self,quizchoice):
    #check firstname, lastname, quiz and score match
        page = top + quiz + bottom
        return page

    @cherrypy.expose
    def gradequizaction(self,option):
    #check firstname, lastname, quiz and score match
        page = top + quizscore + bottom
        return page

    @cherrypy.expose
    def returnstudentaction(self):
        page = top + student + bottom
        return page

    @cherrypy.expose
    def showstudentscoresaction(self,value):
        page = top + studentscore + bottom
        return page

    @cherrypy.expose
    def delstudentaction(self,value):
        # delete student from database
        page = top + delstudent + bottom
        return page

    @cherrypy.expose
    def returneducatoraction(self):
        page = top + educator + bottom
        return page

    @cherrypy.expose
    def addstudentaction(self,fname,lname,email,pword1,pword2):
        # Always escape user input to avoid script injection
        fname = escape(fname)
        lname = escape(lname)
        email = escape(email)
        pword1 = escape(pword1)
        pword2 = escape(pword2)
        match = 'No entry'
        if pword1 !='':
            if pword1==pword2:
                match='Passwords match, record added'
            else:
                match='Passwords do not match, enter again'

        response_body = showname % { # Fill the above html template in
          'fname': fname or 'No entry',
          'lname': lname or 'No entry',
          'email': email or 'No entry',
          'pword1': 'Hidden',
          'pword2': 'Hidden',
          'match': match
        }
        page = top + response_body + bottom
        # add entry to flatfile database
        return page


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(accessdatabase(), '/', conf)
