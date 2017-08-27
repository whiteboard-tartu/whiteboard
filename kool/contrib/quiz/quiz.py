"""
Quiz

A base quiz class, providing some default behaviours that all 
quiz types can inherit or override, as necessary.
"""

class Quiz(object):

	def __init__(self, * args, ** kwargs):
		super().__init__()
		self.name = 
		self.description = 
		self.date_created =
		self.course = 

	def create(self):
		pass

	def read(self):
		pass

	def update(self):
		pass

	def delete(self):
		pass

