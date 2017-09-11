How to Extend Kool
==================

Kool library allows extending of its contrib and storage modules and modifying its behavior. 

Contrib
-------

The contrib module is directory structure is as shown below::

    .
    ├── auth
    │   ├── group.py
    │   ├── hasher.py
    │   ├── permission.py
    │   ├── user.py
    ├── courses
    │   ├── course.py
    └── quizzes
        ├── question.py
        └── quiz.py
    
Below is an example of extending class `User` to `Student`:

>>> from kool.contrib.auth import User
>>> class Student(User):
...   pass
... 
>>> student = Student(first_name='John', last_name='Doe', email='john@doe.com', password='secretpwd')
>>> student.save()
1
>>> 

Storage
-------

Storage provides a way of making data persistent in the Kool library. By default, Kool supports CSV file storage. If you wish to continue storing data with the flatfile database implementation, you can extend the base Storage class and write your preferred implementation.

For example, to create a JSON file storage:

.. code-block:: python

    class JSONStorage(Storage):
        """
        Store the data in a JSON file.
        """

        def __init__(self, path, create_dirs=False, **kwargs):
            """
            Create a new instance.
            Also creates the storage file, if it doesn't exist.
            :param path: Where to store the JSON data.
            :type path: str
            """

            super(JSONStorage, self).__init__()
            touch(path, create_dirs=create_dirs)  # Create file if not exists
            self.kwargs = kwargs
            self._handle = open(path, 'r+')

        def close(self):
            self._handle.close()

        def read(self):
            # Get the file size
            self._handle.seek(0, os.SEEK_END)
            size = self._handle.tell()

            if not size:
                # File is empty
                return None
            else:
                self._handle.seek(0)
                return json.load(self._handle)

        def write(self, data):
            self._handle.seek(0)
            serialized = json.dumps(data, **self.kwargs)
            self._handle.write(serialized)
            self._handle.flush()
            self._handle.truncate()

Much of the storage implementation was borrowed from TinyDB_. So, have a look at it for more examples.

.. References
.. _TinyDB: https://github.com/msiemens/tinydb
