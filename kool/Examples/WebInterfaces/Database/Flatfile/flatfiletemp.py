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
<h2>Choose an option</h2>
<form method="post" action="start">
  Email: <input type="email" name="email"><br>
  Password: <input type="password" name="pword"><br>
  <input type="radio" name="role" value="student" checked>Student<br>
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
<form method="post" action="educator">
  <input type="radio" name="update" value="adduser" checked>Add class member<br>
  <input type="radio" name="update" value="deleteuser">Delete class member<br>
  <input type="radio" name="update" value="updateuser">Update class member grades<br>
  <input type="radio" name="update" value="showuser">Show class member grades<br>
  <input type="radio" name="update" value="makequiz">Make quiz<br>
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
<form method="post" action="student">
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
          <h2>Add user</h2>
            <form method="post" action="generate">
              <p>
                First name: <input type="text" name="fname"><br>
                Last Name: <input type="text" name="lname"><br>
                Email: <input type="email" name="email"><br>
                Password: <input type="password" name="pword1"><br>
                Repeat password: <input type="password" name="pword2">
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

updatestudentscore = """
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
          <h2>Add user</h2>
            <form method="post" action="generate">
              <p>
                First name: <input type="text" name="fname"><br>
                Last Name: <input type="text" name="lname"><br>
                Quiz: <input type="text" name="quiz"><br>
                Score: <input type="text" name="score">
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

showname = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<body>
<h1>Kool</h1>
  <p>
      First name: %(fname)s<br>
      Last name: %(lname)s<br>
      Email: %(email)s<br>
      Passwords : %(match)s
  </p>
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
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

showuser = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

addgrade = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

addgroup = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

delgroup = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

addpermission = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

delpermission = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

haspermission = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
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
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
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
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

takequiz = """
<html>
<head>
<link href="/static/css/style.css" rel="stylesheet">
<link rel="icon"
      type="image/png"
      href="/static/images/logo.png" />
<title>Kool</title>
</head>
<h1>Kool</h1>
<body>
  <p>
      Placeholder for now
   </p>
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
        if pwordemail=='match' & role=='educator':
            return educator
        elif pwordemail=='match' & role=='student':
            return student
        else:
            return startpage

    @cherrypy.expose
    def student(self,option):
        if option=='showmyscores':
            return showmyscores
        else:
            return takequiz

    @cherrypy.expose
    def educator(self,option):
        if option=='addstudent':
            return addstudent
        elif option=='delstudent':
            return delstudent
        elif option=='makequiz':
            return makequiz
        else:
            return updatestudentscore

    @cherrypy.expose
    def updatestudentscore(self,firstname,lastname,quiz,score):
        #check firstname, lastname, quiz and score match
        if options!='match':
            return addstudent
        else:
            return student

    @cherrypy.expose
    def addstudent(self,fname,lname,email,pword1,pword2):
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
