from kool.db.models import Model


class Course(Model):
	"""Course describes a plan of study for a student"""
	
	_courses = {}
	
	def __init__(self, *args, **kwargs):
		super().__init__()
		self.title = ''
		self.description = ''
		self.instructor = None


class Topic(Model):
	"""These are topics that constitute a course"""

	_topics = {}

	def __init__(self, title, description, file, course):
		super().__init__()
		self.title = title
		self.description = description
		self.file = file
		self.course = course