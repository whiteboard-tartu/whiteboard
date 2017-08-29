"""
Quiz

A base quiz class, providing some default behaviours that all 
quiz types can inherit or override, as necessary.
"""
from kool.db.models import Model


class Quiz(Model):

    def __init__(self, * args, ** kwargs):
        super().__init__()
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.course = kwargs['course']
