from kool.db import FlatFileDB


class Course(FlatFileDB):
	"""Course describes a plan of study for a student"""
	
	_courses = {}
	
	def __init__(self, *args, **kwargs):
		super().__init__()
		self.title = ''
		self.description = ''
		self.instructor = None

	def save(self, *args, **kwargs):
		pass

	def delete(self, *args, **kwargs):
		pass


class Topic(FlatFileDB):
	"""These are topics that constitute a course"""

	_topics = {}

	def __init__(self, title, description, file, course):
		super().__init__()
		self.title = title
		self.description = description
		self.file = file
		self.course = course

	def save(self):
		pass

	def delete(self):
		pass
