API documentaiton
=================

``kool.contrib.auth.user``
--------------------------

.. autoclass:: kool.contrib.auth.user
   :members:

``kool.contrib.auth.group``
---------------------------

.. autoclass:: kool.contrib.auth.group
   :members:

``kool.contrib.auth.permission``
--------------------------------

.. autoclass:: kool.contrib.auth.permission
   :members:


``kool.contrib.courses.course``
-------------------------------

.. autoclass:: kool.contrib.courses.course
   :members:
   :special-members:
   :exclude-members: __dict__, __weakref__
   :member-order: bysource

``kool.contrib.quizzes.question``
---------------------------------

.. autoclass:: kool.contrib.quizzes.question
   :members:
   :special-members:
   :exclude-members: __dict__, __weakref__
   :member-order: bysource

``kool.contrib.quizzes.quiz``
-----------------------------

.. autoclass:: kool.contrib.quizzes.quiz
   :members:
   :special-members:
   :exclude-members: __dict__, __weakref__
   :member-order: bysource

``kool.db.flatfile.database``
-----------------------------

.. autoclass:: kool.db.flatfile.database.FlatFileDB
    :members:
    :special-members:
    :exclude-members: __dict__, __weakref__
    :member-order: bysource

.. _table_api:

.. autoclass:: kool.db.flatfile.database.Table
    :members:
    :special-members:
    :exclude-members: __dict__, __weakref__
    :member-order: bysource

.. autoclass:: kool.db.flatfile.database.Record
    :members:
    :special-members:
    :exclude-members: __dict__, __weakref__
    :member-order: bysource

    .. py:attribute:: rid

        The element's id

``kool.db.flatfile.queries``
----------------------------

.. autoclass:: kool.db.flatfile.queries.Query
    :members:
    :special-members:
    :exclude-members: __weakref__
    :member-order: bysource

``kool.db.flatfile.storages``
-----------------------------

.. automodule:: kool.db.flatfile.storages
    :members: CSVStorage
    :special-members:
    :exclude-members: __weakref__

    .. class:: Storage

        The abstract base class for all Storages.

        A Storage (de)serializes the current state of the database and stores
        it in some place (memory, file on disk, ...).

        .. method:: read()

            Read the last stored state.

        .. method:: write(data)

            Write the current state of the database to the storage.

        .. method:: close()

            Optional: Close open file handles, etc.