#!/usr/bin/env python3

"""
A program to check users permissions for a single class
based on encode_grades.py available at
https://bitbucket.org/jjauhien/pygrades/src/

Other references:
https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/
http://www.python-course.eu/python3_dictionaries.php
http://www.tutorialspoint.com/python/python_dictionary.htm
"""
import os
import csv 
from kool.core.exceptions import UserNotFound


class FlatFile(object):

    def get_permissions(self, filename):
        try:
            f = open(filename,'r')
            header = f.readline().rstrip().split(',')
            users = dict()
            for line in f:
                vals = line.split(',')
                username = vals[0]
                realname = vals[1]
                password = vals[2]
                permissions = vals[3]
                users[username] = (realname, password, permissions)
            f.close()
            return header, users
        except IOError:
            print('Error while opening file {0:s}'.format(filename))
            return None

    def add_user(self, username, realname, password, permissions, filename):
        try:
            if os.path.isfile(filename): 
                f = open(filename,'r')
                content = f.read()
                if content.find(username) != -1:
                     print('Error that username already exists')
                     f.close()
                     return None
                else:
                    f.close()
                    f = open(filename,'a')
                    f.write(username + ',' + realname + ',' + password + ',' + permissions)
                    f.close()
                    return None
            else:
                f = open(filename,'w')
                f.write('Username, Real name, password, permissions')
                f.write(username + ',' + realname + ',' + password + ',' + permissions)
                f.close()
                return None
        except IOError:
            print('Error while opening file {0:s}'.format(filename))
            return None
          
    def delete_user(self, username, filename):
        """"
        Deletes user specified by username in the provided file
        """
        try:
            if os.path.isfile(filename):
                reader = csv.reader(open(filename, 'rt'), delimiter=',')
                users = []
                user_found = False

                for row in reader:
                    if row[0] != username:
                        users.append(row)
                    else:
                        user_found = True

                if not user_found:
                    raise UserNotFound

                f = csv.writer(open(filename, 'wt'))
                for user in users:
                    f.writerow(user)
                return None
        except IOError:
            print('Error while opening file {0:s}'.format(filename))
            return None
