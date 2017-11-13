Getting Started
===============

Prerequisites
-------------

1. `Python3 <https://docs.python.org/3/tutorial/>`_

2. `Virtualenv <https://docs.python.org/3/tutorial/venv.html>`_

3. `Pip <https://pip.pypa.io/en/stable/quickstart/>`_

Installing Kool
---------------

To install Kool from PyPI, run::
    
    $ python install kool

If you prefer to install from source, download the latest version from Releases_. Thereafter, extract and run::

    $ python setup.py install


Basic Usage
-----------

The current version support creation of users, courses and quizzes. It also includes a flatfile database implementation of csv storage. The database can be configured as below:: 

    $ vim kool/db/flatfile/database.py 

Under `class FlatFileDB(object):`, set default values as below:: 

    DEFAULT_DB = '<enter database name>'
    DEFAULT_TABLE = '<enter default table name>'
    DEFAULT_STORAGE = <set default storage>

Once you are done with setting default database configs. You can proceed to load classes from the library. For example to initialize class User with some new user, run:

>>> from kool.contrib.auth import User, Group, Permission
>>> user = User(first_name='John', last_name='Doe', email='john@doe.com', password='secretpwd')

To make the record persistent, call save() method for it to be written to a csv file.

>>> user.save()
1
>>> 

Once you have a table object, you can insert records by:

>>> user.insert({'first_name': 'Mary', 'last_name': 'Doe', 'email': 'mary@doe.com', 'password': 'secretpwd'})
2
>>> 

To get all records stored in a table, run:

>>> user.all()
[{'_id': '1', 'email': 'john@doe.com', 'groups': '[]', 'password': 'bcrypt_sha256$$2b$12$8XUv6hUS/Zs7Hjw8U/ArqOHdj/WeutsReeTWgchVpET7HczuMVpIi', 'is_active': 'True', 'last_modified': '2017-09-09 23:18:23.917851', 'first_name': 'John', 'date_created': '2017-09-09 23:18:23.918017', 'last_name': 'Doe', 'permissions': '[]'}, {'_id': '2', 'email': 'mary@doe.com', 'groups': '', 'password': 'secretpwd', 'is_active': '', 'last_modified': '', 'first_name': 'Mary', 'date_created': '', 'last_name': 'Doe', 'permissions': ''}]
>>> 

Passwords are securely stored as a bcrypt sha 256 hash code. 

To filter a specific record from a table, run: 

>>> from kool.db.models import where
>>> user.filter(where('first_name')=='John')
[{'_id': '1', 'email': 'john@doe.com', 'groups': '[]', 'password': 'bcrypt_sha256$$2b$12$8XUv6hUS/Zs7Hjw8U/ArqOHdj/WeutsReeTWgchVpET7HczuMVpIi', 'is_active': 'True', 'last_modified': '2017-09-09 23:18:23.917851', 'first_name': 'John', 'date_created': '2017-09-09 23:18:23.918017', 'last_name': 'Doe', 'permissions': '[]'}]
>>> 

Call the update() method to modify a record:

>>> user.email = 'john@gmail.com'
>>> user.update()
2
>>> user.filter(where('first_name')=='John')
[{'_id': '2', 'email': 'john@gmail.com', 'groups': '[]', 'password': 'bcrypt_sha256$$2b$12$8XUv6hUS/Zs7Hjw8U/ArqOHdj/WeutsReeTWgchVpET7HczuMVpIi', 'is_active': 'True', 'last_modified': '2017-09-09 23:38:12.813258', 'first_name': 'John', 'date_created': '2017-09-09 23:18:23.918017', 'last_name': 'Doe', 'permissions': '[]'}]
>>> 

To delete an existing record:

>>> user.delete()
>>> user.filter(where('first_name')=='John')
[]
>>> 

.. References
.. _Releases: https://github.com/edasi/kool/releases
