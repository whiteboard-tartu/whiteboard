#!/usr/bin/env python

"""
An example demonstrating how to create a web interface to populate flatfile
database using wsgi and python2.

More information on WSGI at:
http://wsgi.readthedocs.io/
https://docs.python.org/3/library/wsgiref.html
http://wsgi.tutorial.codepoint.net/
https://www.toptal.com/python/pythons-wsgi-server-application-interface
"""

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
  <form method="post" action="">
    <p>
      First name: <input type="text" name="fname" value="%(fname)s"><br>
      Last Name: <input type="text" name="lname" value="%(lname)s"><br>
      Email: <input type="email" name="email" value="%(email)s"><br>
      Password: <input type="password" name="pword1" value="%(pword1)s"><br>
      Repeat password: <input type="password" name="pword2" value="%(pword2)s">
    </p>
     <p>
        <input type="submit" value="Submit">
     </p>
  </form>
  <p>
      First name: %(fname)s<br>
      Last name: %(lname)s<br>
      Email: %(email)s<br>
      Match : %(match)s
  </p>
</body>
</html>
"""

def application(environ, start_response):

  # the environment CONTENT_LENGTH may be empty or missing
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except (ValueError):
    request_body_size = 0

  # When the method is POST the variable will be sent
  # in the HTTP requestbody which is passed by the WSGI server
  # in the file like wsgi.input environment variable.
  request_body = environ['wsgi.input'].read(request_body_size)
  d = parse_qs(request_body)

  fname = d.get('fname', [''])[0] # Returns the first age value.
  lname = d.get('lname', [''])[0] # Returns the first age value.
  email = d.get('email', [''])[0] # Returns the first age value.
  pword1 = d.get('pword1', [''])[0] # Returns the first age value.
  pword2 = d.get('pword2', [''])[0] # Returns the first age value.

  # Always escape user input to avoid script injection
  fname = escape(fname)
  lname = escape(lname)
  email = escape(email)
  pword1 = escape(pword1)
  pword2 = escape(pword2)
  match = 'No entry'
  if pword1 !='':
      if pword1==pword2:
          #add record to database
          match='Passwords match, record added'
      else:
          match = 'Passwords do not match, enter again'

  response_body = html % { # Fill the above html template in
    'fname': fname or 'No entry',
    'lname': lname or 'No entry',
    'email': email or 'No entry',
    'pword1': 'Hidden',
    'pword2': 'Hidden',
    'match': match
  }

  status = '200 OK'

  response_headers = [
    ('Content-Type', 'text/html'),
    ('Content-Length', str(len(response_body)))
  ]

  start_response(status, response_headers)
  return [response_body]f

httpd = make_server('localhost', 8051, application)
httpd.serve_forever()
