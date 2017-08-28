import os
import csv
from abc import ABCMeta, abstractmethod
from os.path import basename

from .utils import with_metaclass, touch, mkdir


class Storage(with_metaclass(ABCMeta, object)):
    """
    The abstract base class for all Storages.

    A Storage (de)serializes the current state of the database and stores it in
    some place (memory, file on disk, ...).
    """

    @abstractmethod
    def read(self):
        """
        Read the last stored state.

        Any kind of deserialization should go here.
        Return ``None`` here to indicate that the storage is empty.

        Decorators:
            abstractmethod
        
        Raises:
            NotImplementedError
        """
        raise NotImplementedError('Implement read operation!')

    @abstractmethod
    def write(self, data):
        """
        Write the current state of the database to the storage.

        Any kind of serialization should go here.

        Decorators:
            abstractmethod
        
        Arguments:
            data {dict} -- The current state of the database.
        
        Raises:
            NotImplementedError
        """
        raise NotImplementedError('Implement write operation!')

    def close(self):
        """
        Optional: Close open file handles, etc.
        """
        pass


class CSVStorage(Storage):
    """
    Store the data in a CSV file.
    """

    def __init__(self, path, init_db=True, create_dirs=False, **kwargs):
        """
        Create a new csv storage instance.

        Also creates the storage file, if it doesn't exist.

        Arguments:
            path {str} -- Where to store the JSON data.
            **kwargs -- extra options
        
        Keyword Arguments:
            create_dirs {bool} -- option to create directories (default: {False})
        """
        super(CSVStorage, self).__init__()
        
        self.kwargs = kwargs

        # Initialize database
        if init_db:
            self.path = os.path.dirname(path)
        #     mkdir(self.path)
        #     return

        base = basename(path)
        base_ext = os.path.splitext(base)[1]
        if not base_ext:
            path += '.csv'

        # Create file if not exists
        touch(path, create_dirs=create_dirs)
        
        # Opens the file in read and write mode
        self._handle = open(path, 'r+')

    def read(self):
        # Get the file size
        self._handle.seek(0, os.SEEK_END)
        size = self._handle.tell()

        if not size:
            # File is empty
            return None
        else:
            self._handle.seek(0)
            csv_file = csv.DictReader(self._handle, delimiter=',', quotechar='"')
            
            data = {}
            for row in csv_file:
                data[row['_id']]=row
            
            return data

    def write(self, data):
        self._handle.seek(0)
        
        # data = file[filename]
        frow = None
        
        # Retrieve column names from first record
        for key, values in data.items():
            frow = values
            break

        if data and frow:
            header_set = {'_id'}  # initialize header set with _id
            header_set.update(set(list(frow.keys())))
            header = list(header_set)
            header.sort()

            csvwriter = csv.DictWriter(self._handle, delimiter=',', 
                fieldnames=header)
            csvwriter.writeheader()
            for key, values in data.items():
                values['_id'] = key
                csvwriter.writerow(values)
            
            self._handle.flush()
            self._handle.truncate()

    def close(self):
        self._handle.close()
