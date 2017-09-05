Welcome to Kool's documentation!
================================

Kool is an open source platform for online classroom management. 

This project focus is to create a minimalist framework that educationist can extend when building an online classroom management system. Below is an example of extending class User to Student and instantiating a student object.

>>> from kool.contrib.auth import User
>>> class Student(User):
...   pass
... 
>>> student = Student(first_name='John', last_name='Doe', email='john@doe.com', password='secretpwd')
>>> student.save()
1
>>> 



User's Guide
------------

.. toctree::
   :maxdepth: 2

   intro
   getting-started
   usage

Extending Kool
----------------

.. toctree::
   :maxdepth: 2

   Extending Kool <extend>

API Reference
-------------

.. toctree::
   :maxdepth: 2

   api

Additional Notes
----------------

.. toctree::
   :maxdepth: 2

   contribute
   changelog
   Upgrade Notes <upgrade>
