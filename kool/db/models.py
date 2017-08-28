
from .flatfile import FlatFileDB
from kool.utils import camel_to_snake, now


class Model(object):
    db = None  # database

    def __init__(self, * args, ** kwargs):
        # Instantiate database
        Model.db = FlatFileDB()
        # Get class name
        cls_name = self.__class__.__name__
        table_name = camel_to_snake(cls_name)
        self._table = Model.db.create_table(name=table_name) 
        self.last_modified = None
        self.date_created = None

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
        obj_id = self._table.insert(data)
        return obj_id

    def delete(self, * args, ** kwargs):
        pass

    def purge(self, * args, ** kwargs):
        pass

    def props(self):
        """Converts object to dictionary"""
        return dict(
            (key, value) 
            for (key, value) in self.__dict__.items() 
            if not (key.startswith('_') or key.startswith('__')))
