:tocdepth: 3

Advanced Usage
==============

Kool has a `models.py` file that allows database operations to be applied on a class that inherits from it. 

To get a table object:

>>> from kool.db.models import table
>>> from kool.contrib.auth import User
>>> user_table = table(User)


Queries
-------

Queries can be used in two ways: 

1) ORM-like usage:

>>> User = Query()
>>> table.filter(User.first_name == 'John')
>>> table.filter(User['last_name'] == 'Doe')

2) Classical usage:

>>> table.filter(where('value') == True)

Note that ``where(...)`` is a shorthand for ``Query(...)`` allowing for
a more fluent syntax.

Besides the methods documented here you can combine queries using the
binary AND and OR operators:

>>> table.filter(where('field1').exists() & where('field2') == 5)  # Binary AND
>>> table.filter(where('field1').exists() | where('field2') == 5)  # Binary OR

Queries are executed by calling the resulting object. They expect to get the
element to test as the first argument and return ``True`` or ``False``
depending on whether the elements matches the query or not.

