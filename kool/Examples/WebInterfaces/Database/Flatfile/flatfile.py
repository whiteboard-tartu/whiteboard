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

startpage = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<body>
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
<h2>Login</h2>
<form method="post" action="start">
  Email:<br> <input type="email" name="email"><br>
  Password:<br> <input type="password" name="pword"><br>
  <input type="radio" name="role" value="student" checked>Student
  <input type="radio" name="role" value="educator">Educator<br>
  <input type="submit" value="Submit">
</form>
<footer>
<img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
</footer>
</body>
</html>
"""

educator = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<body>
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
<h2>Choose an option</h2>
<form method="post" action="educatoraction">
  <input type="radio" name="option" value="addstudent" checked>Add class member<br>
  <input type="radio" name="option" value="delstudent">Delete class member<br>
  <input type="radio" name="option" value="showstudentscore">Show class member grades<br>
  <input type="radio" name="option" value="makequiz">Make multiple choice quiz<br>
  <input type="submit" value="Submit">
</form>
<footer>
<img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
</footer>
</body>
</html>
"""

student = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<body>
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
<h2>Choose an option</h2>
<form method="post" action="studentaction">
  <input type="radio" name="option" value="showmyscores">Show my scores<br>
  <input type="radio" name="option" value="takequiz">Take quiz<br>
  <input type="submit" value="Submit">
</form>
<footer>
<img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
</footer>
</body>
</html>
"""

addstudent = """
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
    <footer>
    <img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
    </footer>
    </body>
    </html>
"""

showstudentscore = """
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
    <footer>
    <img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
    </footer>
    </body>
    </html>
"""

delstudent = """
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
    <footer>
    <img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
    </footer>
    </body>
    </html>
"""

showmyscores = """
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
          <h2>My quiz scores</h2>
            <form method="post" action="showmyscoresaction">
              <p>
                Placeholder for now - get scores from database and display them
                </p>
              <p>
                 <input type="submit" value="Submit">
              </p>
            </form>
    <footer>
    <img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
    </footer>
    </body>
    </html>
"""

makequiz = """
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
          <h2>Make quiz</h2>
            <form method="post" action="makequizaction">
              <p>
                <p>
                  New quiz name:<br> <input type="text" name="qname"><br>
                  Multiple choice options per question:<br> <input type="number" name="options"><br>
                  </p>
                </p>
              <p>
                 <input type="submit" value="Add questions">
              </p>
            </form>
    <footer>
    <img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
    </footer>
    </body>
    </html>
"""

addquizquestion = """
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
    <footer>
    <img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
    </footer>
    </body>
    </html>
"""

choosequiz = """
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
    <footer>
    <img src="/static/images/TartuMain.jpg" alt="University of Tartu main building" style="height:256px;">
    </footer>
    </body>
    </html>
"""

class accessdatabase(object):
    @cherrypy.expose
    def index(self):
        return startpage

    @cherrypy.expose
    def start(self,email,pword,role):
      # check password is correct one for supplied email address
        pwordemail='match'
        if ((pwordemail=='match') & (role=='educator')):
            return educator
        elif ((pwordemail=='match') & (role=='student')):
            return student
        else:
            return startpage

    @cherrypy.expose
    def studentaction(self,option):
        if option=='showmyscores':
            return showmyscores
        else:
            return choosequiz

    @cherrypy.expose
    def educatoraction(self,option):
        print(option)
        if option=='addstudent':
            return addstudent
        elif option=='delstudent':
            return delstudent
        elif option=='makequiz':
            return makequiz
        elif option=='showstudentscore':
            return showstudentscore
        else:
            return addstudentscore

    @cherrypy.expose
    def updatestudentscore(self,firstname,lastname,quiz,score):
        #check firstname, lastname, quiz and score match
        if options!='match':
            return addstudent
        else:
            return student

    @cherrypy.expose
    def makequizaction(self,qname,options):
    #check firstname, lastname, quiz and score match
        return addquizquestion

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
        # add entry to flatfile database
        return response_body


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
