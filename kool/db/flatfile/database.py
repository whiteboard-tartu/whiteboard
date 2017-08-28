"""
FlatFileDB

This is a simple flat file database implementation. 

FlatFileDB is a variant of TinyDB that focuses on csv storage.
TinyDB is a lightweight document oriented database written in pure 
python with no external depedencies.

Repo: https://github.com/msiemens/tinydb
"""
import os
from . import CSVStorage
from .utils import LRUCache, iteritems, itervalues

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Element(dict):
    """
    Represents an element stored in the database.

    This is a transparent proxy for database elements. It exists
    to provide a way to access an element's id via ``el.eid``.
    """
    def __init__(self, value=None, eid=None, **kwargs):
        super(Element, self).__init__(**kwargs)

        if value is not None:
            self.update(value)
            self.eid = eid


class StorageProxy(object):
    
    def __init__(self, flatfiledb, table_name):
        self._database = flatfiledb._database
        self._storage = flatfiledb._storage
        self._table_name = table_name
        
        # Prepare the storage 
        self._opened = True

        # Initialize a table
        table_path = os.path.join(self._database.path, self._table_name)
        self._table = self._storage(table_path,  create_dirs=True)

    def read(self):
        try:
            raw_data = self._table.read() or {}
        except KeyError:
            return {}

        data = {}
        for key, val in iteritems(raw_data):
            eid = int(key)
            data[eid] = Element(val, eid)

        return data

    def write(self, values):
        data = self._table.read() or {}
        self._table.write(values)

    def purge_table(self):
        try:
            self._table.write({})
        except KeyError:
            pass

    def close(self):
        self._opened = False
        self._table.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self._opened is True:
            self.close()


class FlatFileDB(object):
    """
    FlatFileDB database main class. 

    Provides access to methods of operating the database.     
    """
    DEFAULT_DB = '.ffdb'
    DEFAULT_TABLE = '_default_table'
    DEFAULT_STORAGE = CSVStorage
    _storage = None
    _database = None

    def __init__(self, name=DEFAULT_DB, **options):
        """
        Create a new database.
        
        All arguments and keyword arguments will be passed to the underlying
        storage class
        """
        self.name = name

        storage = options.pop('storage', FlatFileDB.DEFAULT_STORAGE)
        table = options.pop('default_table', FlatFileDB.DEFAULT_TABLE)
        db_path = os.path.join(PROJECT_ROOT, self.name)
        # path = options.pop('path', os.path.join(DB_PATH, table))

        # Prepare the storage 
        self._opened = True
        
        # Define storage
        FlatFileDB._storage = storage

        # Create database
        FlatFileDB._database = storage(os.path.join(db_path, '.meta'), 
            init_db=True, create_dirs=True, **options)
        
        self._table_cache = {}
        
        # Define tables
        self._tables = {}
        self._table = None

        data = FlatFileDB._database.read() or {}
        if data:
            self._last_id = max(i for i in data)
        else:
            self._last_id = 0

    def create_table(self, name=DEFAULT_TABLE, **options):
        """
        Creates a new table, if it doesn't exist, otherwise
        it returns the cached table.
        
        Arguments:
            **options {[type]} -- [description]
        
        Keyword Arguments:
            name {str} -- provide table name (default: {DEFAULT_TABLE})
        """
        if name in self._table_cache:
            return self._table_cache[name]

        self._table = self.table_class(StorageProxy(FlatFileDB, name), **options)

        self._table_cache[name] = self._table

        self._tables[self._get_next_id()] = {'table': name}
        FlatFileDB._database.write(self._tables)
        
        return self._table

    def table(self, name=DEFAULT_TABLE, **options):
        """
        Get access to a specific table.
        
        Arguments:
            **options -- extra options
        
        Keyword Arguments:
            name {str} -- the name of the table (default: {DEFAULT_TABLE})
        
        Returns:
            table -- a table object
        """
        if name in self._table_cache:
            return self._table_cache[name]._read()

        self._table = self.table_class(StorageProxy(FlatFileDB, name), **options)

        return self._tables._read()

    def tables(self):
        """
        Get a list of table objects.
        
        Returns:
            [set[Table]] -- a set of table names
        """
        # return set(self._storage.read()) if self._storage.read() else None
        return self._tables

    def purge_table(self, name):
        """Purge a specific table from the database. **CANNOT BE REVERSED!**
        
        Arguments:
            name {str} -- table name
        """
        if name in self._table_cache:
            del self._table_cache[name]

        proxy = StorageProxy(FlatFileDB, name)
        proxy.purge_table()

    def close(self):
        self._opened = False
        self._table.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self._opened is True:
            self.close()

    def _get_next_id(self):
        """
        Increment the ID used the last time and return it.
        """
        current_id = int(self._last_id) + 1
        self._last_id = current_id

        return current_id

    # def __getattr__(self, name):
    #     """
    #     Forward all unknown attribute calls to the underlying standard table.
    #     """
    #     return getattr(self._table, name)

    def __len__(self):
        """
        Get the total number of elements in the database.
        """
        return len(self._tables)
    
    
class Table(object):
    """
    Represents a single FlatFileDB table
    """

    def __init__(self, storage, cache_size=10):
        """
        Initialize a table
        
        Arguments:
            storage {StorageProxy} -- access to the storage
        
        Keyword Arguments:
            cache_size {number} -- Maximum size of query cache (default: {10})
        """
        self._storage = storage
        self._query_cache = LRUCache(capacity=cache_size)
        self.name = self._storage._table_name

        data = self._read()
        if data:
            self._last_id = max(i for i in data)
        else:
            self._last_id = 0

    def __str__(self):
        return '{}'.format(self.name)

    def process_elements(self, func, cond=None, eids=None):
        """
        Helper function for processing all elements specified by condition
        or IDs.
        
        The function passed as ``func`` has to be a callable. It's first
        argument will be the data currently in the database. It's second
        argument is the element ID of the currently processed element.
        
        Arguments:
            func {[type]} -- the function to execute on every included element.
                             first argument: all data
                             second argument: the current eid
        
        Keyword Arguments:
            cond {Query} -- condition to be applied (default: {None})
            eids {list} -- elements to use (default: {None})
        
        Returns:
            [list] -- the element IDs that were affected during processing
        """
        data = self._read()

        if eids is not None:
            # Processed element specified by id
            for eid in eids: 
                func(data, eid)

        else:
            # Collect affected eids
            eids = []

            # Processed elements specified by condition 
            if eid in list(data):
                if cond(data[eid]):
                    func(data, eid)
                    eids.append(eid)

        self._write(data)

        return eids

    def clear_cache(self):
        """Clear the query cache.
        
        A simple helper that clears the internal query cache.
        """
        self._query_cache.clear()

    def _get_next_id(self):
        """
        Increment the ID used the last time and return it.
        """
        current_id = self._last_id + 1
        self._last_id = current_id

        return current_id

    def _read(self):
        """
        Reading access to the database.
        
        Returns:
            [dict] -- all values
        """
        return self._storage.read()

    def _write(self, values):
        """
        Writing acccess to the database.
        
        Arguments:
            values {dict} -- the new values to write
        """
        self._query_cache.clear()
        self._storage.write(values)

    def __len__(self):
        """Get the total number of elements in a table"""
        return len(self._read())

    def all(self):
        """
        Get all elements stored in the table.
        
        Returns:
            [list] -- a list with all elements.
        """
        return list(itervalues(self._read()))

    def __iter__(self):
        """
        Iterate over all elements stored in the table.
        
        Yields:
            [listiterator[Element]] -- an iterator over all elements.
        """
        for value in itervalues(self._read()):
            yield value

    def insert(self, element):
        """
        Insert a nwe element into the table.
        
        Arguments:
            element {dict} -- the element to insert
        
        Returns:
            [int] -- the inserted element's ID
        
        Raises:
            ValueError -- Element is not a dictionary
        """
        eid = self._get_next_id()

        if not isinstance(element, dict):
            raise ValueError('Element is not a dictionary')

        data = self._read()
        data[eid] = element
        self._write(data)

        return eid

    def insert_multiple(self, elements):
        """
        Insert multiple elements into the table.
        
        Arguments:
            elements {list} -- a list of elements to insert
        
        Returns:
            [list] -- a list containing the inserted elements IDs
        """
        eids = []
        data = self._read()

        for element in elements: 
            eid = self._get_next_id()
            eids.append(eid)

            data[eid] = element

        self._write(data)

        return eids

    def remove(self, cond=None, eids=None):
        """
        Remove all matching elements.
        
        Keyword Arguments:
            cond {Query} -- the condition to check against (default: {None})
            eids {list} -- list of element IDs (default: {None})
        
        Returns:
            [list] -- a list containing the removed element's ID
        """
        return self.process_elements(
            lambda data, eid: data.pop(eid), cond, eids)

    def update(self, fields, cond=None, eids=None):
        """
        Update all matching elements to have a given set of fields.
        
        Arguments:
            fields {dict} -- the fields that the matching elements will
                                have or a method that will update the elements
        
        Keyword Arguments:
            cond {Query} -- which elements to update (default: {None})
            eids {list} -- a list of element IDs (default: {None})
        
        Returns:
            [list] -- a list containing the updated element's ID
        """
        if callable(fields):
            return self.process_elements(
                lambda data, eid: fields(data[eid]), cond, eids)
        else:
            return self.process_elements(
                lambda data, eid: data[eid].update(fields), cond, eids)
    
    def purge(self):
        """Purge the table by removing all elements"""
        self._write({})
        self._last_id = 0

    def filter(self, cond):
        """
        Filter all elements by matching condition
        
        Arguments:
            cond {Query} -- the condition to check against.
        
        Returns:
            [list[Element]] -- list of matching elements
        """
        if cond in self._query_cache:
            return self._query_cache[cond][:]

        elements = [element for element in self.all() if cond(element)]
        self._query_cache[cond] = elements

        return elements[:]

    def get(self, cond=None, eid=None):
        """
        Get exactly one element by matching condition.
        
        Keyword Arguments:
            cond {Query} -- the condition to check against (default: {None})
            eid {int} -- the element's ID  (default: {None})
        
        Returns:
            [Element | None] -- the element or None
        """
        if eid is not None: 
            return self._read().get(eid, None)

        # Get element by condition
        for element in self.all():
            if cond(element):
                return element

    def count(self, cond):
        """
        Count all elements matching a condition.
        
        Arguments:
            cond {Query} -- the condition 
        
        Returns:
            [int] -- integer value of the count
        """

        return len(self.filter(cond))

    def contains(self, cond=None, eids=None):
        """
        Checks whether the database has an element matching a consition or ID.
        
        If ``eids`` is set, it checks if the db contains an element with one
        of the specified.

        Keyword Arguments:
            cond {Query} -- the condition (default: {None})
            eids {list} -- the element IDs (default: {None})
        
        Returns:
            [Element | None] -- the element or None
        """
        if eids is not None:
            # Elements specified by ID
            return any(self.get(eid=eid) for eid in eids)

        return self.get(cond) is not None

# Set the default table class
FlatFileDB.table_class = Table
