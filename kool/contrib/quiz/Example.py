#!/usr/bin/env python
# References
#
# http://www.techteachers.co.za/2015/07/multiple-choice-quiz-using-python/
# http://wsgi.tutorial.codepoint.net/
# https://www.w3schools.com/html/html_forms.asp

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="get" action="">
        <p>
          What is the largest ocean in the world? 
        </p>
        <p>
            Oceans:
            <input
                name="oceans" type="radio" value="Indian"
                %(checked-Indian)s
            > The Indian Ocean
            <input
                name="oceans" type="radio" value="Pacific"
                %(checked-Pacific)s
            > The Pacific Ocean
            <input
                name="oceans" type="radio" value="Atlantic"
                %(checked-Atlantic)s
            > The Atlantic Ocean
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>
        Your answer %(oceans)s is %(correctness)s
    </p>
</body>
</html>
"""

def application (environ, start_response):

    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    # As there can be more than one value for a variable then
    # a list is provided as a default value.
    oceans = d.get('oceans', []) # Returns a list of oceans

    # Always escape user input to avoid script injection
    oceans = [escape(ocean) for ocean in oceans]

    print oceans

    if ('Pacific' in oceans):
        correctness='right'
        print 'right'
    else:
        correctness='wrong'
        print 'wrong'

    response_body = html % { # Fill the above html template in
        'checked-Indian': ('', 'checked')['checked' in oceans],
        'checked-Pacific': ('', 'checked')['checked' in oceans],
        'checked-Atlantic': ('', 'checked')['checked' in oceans],
        'correctness': correctness or ['Empty'],
        'oceans': ', '.join(oceans or ['No answer yet'])
    }

    status = '200 OK'

    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

httpd = make_server('localhost', 8051, application)

# Now it is serve_forever() in instead of handle_request()
httpd.serve_forever()
