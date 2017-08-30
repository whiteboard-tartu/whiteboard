from kool.db.models import Model

class Group(Model):
	"""
	Groups are used to cluster similar users.

	Extends:
		Model
	"""

	def __init__(self, name):
		super().__init__()
		self.name = name
		self.permissions = []

	def add_permissions(self, perm):
		if not perm in self.permissions:
			self.permissions.append(perm)

