Welcome to Kool's documentation!
================================

Kool is an open source platform for online classroom management. 

This project focus is to create a minimalist framework that educationist can extend when building an online classroom management system.

>>> from kool.contrib.auth import User
>>> tbl_user = User(first_name='Antony', last_name='Orenge', email='antony@test.com', password='secretpwd')
>>> tbl_user.save()
1
>>> tbl_user.insert({'first_name': 'Mary', 'last_name': 'Doe', 'email': 'mary@doe.com', 'password': 'secretpwd2'})
2


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
