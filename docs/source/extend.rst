How to Extend Kool
==================

Below is an example of extending class User to Student and instantiating a student object.

>>> from kool.contrib.auth import User
>>> class Student(User):
...   pass
... 
>>> student = Student(first_name='John', last_name='Doe', email='john@doe.com', password='secretpwd')
>>> student.save()
1
>>> 
