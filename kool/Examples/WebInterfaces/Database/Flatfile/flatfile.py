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

getname = """
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

class AddName(object):
    @cherrypy.expose
    def index(self):
        return getname

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
    cherrypy.quickstart(AddName())
