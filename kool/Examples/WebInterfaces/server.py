#!/usr/bin/env python3

"""
An example demonstrating how to create a web interface to populate a flatfile
database using cherrypy and python3

This version in progress to match presentation setup

More information on cherrypy at:
http://docs.cherrypy.org/en/latest/tutorials.html

"""
import os
import string
import cherrypy
import templates as t
from cgi import parse_qs, escape


class Server(object):

    @cherrypy.expose
    def index(self):
        page = t.HEADER + t.LOGIN_FORM + t.FOOTER
        return page

    @cherrypy.expose
    def start(self, email, pword, role):
        # check password is correct one for supplied email address
        pwordemail = 'match'
        if ((pwordemail == 'match') & (role == 'educator')):
            return self.educator_options()
        elif ((pwordemail == 'match') & (role == 'student')):
            return self.student_options()
        else:
            return self.index()

    @cherrypy.expose
    def student(self, option):
        if option == 'show_my_scores':
            page = t.HEADER + t.NAVBAR + t.START_CONTAINER + t.SHOW_MY_SCORE + t.END_CONTAINER + t.FOOTER
            return page
        else:
            page = t.HEADER + t.NAVBAR + t.START_CONTAINER + t.CHOOSE_QUIZ + t.END_CONTAINER + t.FOOTER
            return page

    @cherrypy.expose
    def educator(self, option):
        if option == 'add_student':
            return self.add_student_form()
        elif option == 'del_student':
            return self.del_student_form()
        elif option == 'make_quiz':
            return self.make_quiz_form()
        else:
            return self.show_students_scores()

    @cherrypy.expose
    def add_student_form(self):
      return t.HEADER + t.NAVBAR + t.START_CONTAINER + t.ADD_STUDENT + t.END_CONTAINER + t.FOOTER

    @cherrypy.expose
    def del_student_form(self):
      return t.HEADER + t.NAVBAR + t.START_CONTAINER + t.DELETE_STUDENT + t.END_CONTAINER + t.FOOTER

    @cherrypy.expose
    def make_quiz_form(self):
      return t.HEADER + t.NAVBAR + t.START_CONTAINER + t.MAKE_QUIZ + t.END_CONTAINER + t.FOOTER

    @cherrypy.expose
    def make_quiz(self, qname, numquestions, numoptions):
        QUIZ_OPTIONS = t.QUIZ_OPTIONS_START
        for nn in range(0, int(numquestions)):
            QUIZ_OPTIONS = QUIZ_OPTIONS + t.NEW_QUESTION
            for n in range(0, int(numoptions)):
                QUIZ_OPTIONS = QUIZ_OPTIONS + t.QUIZ_OPTION
        QUIZ_OPTIONS = QUIZ_OPTIONS + t.QUIZ_OPTIONS_END

        #setup forms apporpriately to write to database
        page = t.HEADER + QUIZ_OPTIONS + t.FOOTER
        return page

    @cherrypy.expose
    def choose_quiz(self, quizchoice):
        #check firstname, lastname, quiz and score match
        page = t.HEADER + t.QUIZ_PAGE + t.FOOTER
        return page

    @cherrypy.expose
    def grade_quiz(self, option):
        #check firstname, lastname, quiz and score match
        page = t.HEADER + t.QUIZ_SCORE + t.FOOTER
        return page

    @cherrypy.expose
    def student_options(self):
        page = t.HEADER + t.NAVBAR + t.START_CONTAINER + t.STUDENT_FORM + t.END_CONTAINER + t.FOOTER
        return page

    @cherrypy.expose
    def show_students_scores(self):
        return t.HEADER + t.NAVBAR + t.START_CONTAINER + t.SHOW_STUDENT_SCORES + t.END_CONTAINER + t.FOOTER

    @cherrypy.expose
    def delete_student(self, value):
        # choose student to delete from database
        page = t.HEADER + t.DELETE_STUDENT + t.FOOTER
        return page

    @cherrypy.expose
    def display_student_scores(self,value):
            page = t.HEADER + t.DISPLAY_STUDENT_SCORES + t.FOOTER
            return page

    @cherrypy.expose
    def complete_delete_student(self,value):
        # delete t.STUDENT_FORM from database
        page = t.HEADER + t.COMPLETE_DELETE_STUDENT + t.FOOTER
        return page

    @cherrypy.expose
    def educator_options(self):
        page = t.HEADER + t.NAVBAR + t.START_CONTAINER + t.EDUCATOR_FORM + t.END_CONTAINER + t.FOOTER
        return page

    @cherrypy.expose
    def add_student(self, fname, lname, email, pword1, pword2):
        # Always escape user input to avoid script injection
        fname = escape(fname)
        lname = escape(lname)
        email = escape(email)
        pword1 = escape(pword1)
        pword2 = escape(pword2)
        match = ''

        if pword1 != pword2:
            match = 'Passwords do not match, enter again'

        if not match:
          response_body = t.SHOW_STUDENT.format(
            fname or 'No entry',
            lname or 'No entry',
            email or 'No entry',
          )
          return t.HEADER + t.NAVBAR + t.START_CONTAINER + response_body + t.END_CONTAINER + t.FOOTER
        else:
          response_body = t.ERROR_MSG.format(match)
          return t.HEADER + t.NAVBAR + t.START_CONTAINER + response_body + t.ADD_STUDENT + t.END_CONTAINER + t.FOOTER


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/assets': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './assets'
        }
    }
    cherrypy.quickstart(Server(), '/', conf)
