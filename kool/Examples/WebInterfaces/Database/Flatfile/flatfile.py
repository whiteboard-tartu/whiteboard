#!/usr/bin/env python3

"""
An example demonstrating how to create a web interface to populate a flatfile
database using cherrypy and python3

More information on cherrypy at:
http://docs.cherrypy.org/en/latest/tutorials.html

"""
import string
import cherrypy
from cgi import parse_qs, escape

startpage = """
<html>
<head></head>
<body>

<form method="post" action="start">
  <input type="radio" name="update" value="adduser" checked> Add class member<br>
  <input type="radio" name="update" value="deleteuser"> Delete class member<br>
  <input type="radio" name="update" value="updateuser"> Update class member grades<br>
  <input type="radio" name="update" value="showuser"> Show class member grades<br>
  <input type="submit" value="Submit">
</form>

</body>
</html>
"""

addname = """
<html>
<head></head>
          <body>
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
          </body>
    </html>
"""

showname = """
<html>
<body>
  <p>
      First name: %(fname)s<br>
      Last name: %(lname)s<br>
      Email: %(email)s<br>
      Passwords : %(match)s
  </p>
</body>
</html>
"""

delname = """
<html>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

showuser = """
<html>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

addgrade = """
<html>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

addgroup = """
<html>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

delgroup = """
<html>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

addpermission = """
<html>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

delpermission = """
<html>
<body>
  <p>
      Placeholder for now
   </p>
</body>
</html>
"""

haspermission = """
<html>
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
    def start(self,update):
        if update=='adduser':
            return addname
        elif update=='deleteuser':
            return delname
        elif update=='showuser':
            return showuser
        else:
            return addgrade

    @cherrypy.expose
    def generate(self,fname,lname,email,pword1,pword2):
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
                match = 'Passwords do not match, enter again'

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
    cherrypy.quickstart(accessdatabase())
