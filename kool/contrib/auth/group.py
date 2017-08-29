from kool.db.models import Model

class Group(Model):
	"""Groups are used to cluster similar users."""
	
	_groups = {}

	def __init__(self, name):
		super().__init__()
		self._name = name
		self._permissions = []

	@property
	def permissions(self):
		return self._permissions

	@permissions.setter
	def permissions(self, perm):
		if not perm in self._permissions:
			self._permissions.append(perm)

