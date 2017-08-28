from .flatfile import FlatFileDB
from kool.utils import camel_to_snake, now


class Model(object):
    db = None  # database

    def __init__(self, * args, ** kwargs):
        """
        Model provides save, delete, purge operations to every
        class that inherits it.
        """
        # Instantiate database
        Model.db = FlatFileDB()

        # Get class name, so as to set the table name
        cls_name = self.__class__.__name__
        table_name = camel_to_snake(cls_name)
        self._table = Model.db.create_table(name=table_name) 
        self.last_modified = None
        self.date_created = None
        self._id = None

    def save(self, * args, ** kwargs):
        """
        Saves current object to database.
        It also updates the `last_modified` and `date_created` fields.
        """
        data = {}
        self.last_modified = '{}'.format(now())
        if not self.date_created:
            self.date_created = '{}'.format(now())
        # get objects dict
        data = self.props()

        # dumps dict to database
        self._id = self._table.insert(data)
        return self._id

    def delete(self, * args):
        eids = []

        eids = list(args) or ([self._id,] if self._id else [])
        if eids:
            self._table.remove(eids=eids)
        else:
            raise ValueError('Object must be saved to delete')

    def purge(self, confirm=False):
        """
        Truncates the table. Operation is irreversible.
        
        Keyword Arguments:
            confirm {bool} -- user confirmation (default: {False})
        """
        if confirm:
            self._table.purge()
        else:
            raise ValueError('Confirm argument has to be set true')

    def props(self):
        """Converts object to dictionary"""
        return dict(
            (key, value) 
            for (key, value) in self.__dict__.items() 
            if not (key.startswith('_') or key.startswith('__')))
