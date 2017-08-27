from kool.db import FlatFileDB

class Group(FlatFileDB):
	"""Groups are used to cluster similar users."""
	
	_groups = {}

	def __init__(self, name):
		super().__init__()
		self._name = name
		self._permissions = []

	def save(self):
		pass

	def delete(self):
		pass

	@property
	def permissions(self):
		return self._permissions

	@permissions.setter
	def permissions(self, perm):
		if not perm in self._permissions:
			self._permissions.append(perm)

