:tocdepth: 3


Advanced Usage
==============

Kool has a `models.py` file that allows database operations to be applied on a class that inherits from it. 
Look at the `models` API for allowed operations.

Table
-----

Table is composed of records which are made up of multiple fields. Each `Record` is identified by `rid` which is a proxy to the `_id` field in the table files. In this flat file database implementation, every table represents a file. Multiple files makeup a database. The `Table` class provides methods to perform CRUD and Query operations on its data.  

To obtain a `Table` object without instantiating the class you can use the class method `table()` which takes a class as an argument and returns an equivalent `Table` object of the class:

>>> from kool.db.models import table
>>> from kool.contrib.auth import User
>>> user_table = table(User)


Queries
-------

Queries allows data to be requested from a table or combination of tables. The result is generated as list of flatfile records. To query a table, you need an object of type `Table`. 

Query operations include providing a condition as an argument to query methods `any()`, `filter()`, `matches()`, and `all()`. Conditions are made up by comparing values using binary operators (`==`, `<`, `>`, `>=`, `<=`, `~`). Two ways of performing queries are:

1) Classical style:

>>> from kool.db.models import where
>>> user_table.filter(where('value') == True)

2) ORM-like style:

>>> from kool.db.models import Query
>>> User = Query()
>>> user_table.filter(User.first_name == 'John')
>>> user_table.filter(User['last_name'] == 'Doe')
>>> user_table.filter(User.age >= 21)

Advanced queries
----------------

Additionally, you can perform complex queries by using logical expressions to modify or combine queries as show below: 

>>> # Logical AND:
>>> user_table.filter((User.name == 'John') & (User.age <= 26))

>>> # Logical OR:
>>> user_table.filter((User.name == 'John') | (User.name == 'Mary'))

Other operations that can be performed include:

Check the existence of a field:

>>> user_table.filter(User.first_name.exists())

Perform a Regular expression. The field has to match the regex:

>>> user_table.filter(User.first_name.matches('[aZ]*'))

Perform a Custom test:

>>> test_func = lambda s: s == 'John'
>>> user_table.filter(User.first_name.test(test_func))

Custom test with parameters:

>>> def test_func(val, m, n):
>>>     return m <= val <= n
>>> user_table.filter(User.age.test(test_func, 18, 21))
>>> user_table.filter(User.age.test(test_func, 21, 30))

.. note::

    When using ``&`` or ``|``, make sure you wrap the conditions on both sides with parentheses or Python will mess up the comparison.
