from kool.db.models import Model
from kool.contrib.auth.hasher import make_password, check_password


class User(Model):
    """Base class for users"""
    
    def __init__(self, * args, **kwargs):
        super().__init__()
        self.email = kwargs['email']
        self.password = kwargs['password']
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.is_active = True
        self.groups = []
        self.permissions = []

    def set_password(self, raw_password):
        """Return encoded password"""
        self.password = make_password(raw_password)
        print(self.password)

    def check_password(self, raw_password):
        """Checks if the password matches correctly"""

        def setter(raw_password):
            self.set_password(raw_password)

        return check_password(raw_password, self.password, setter) 

    def add_groups(self, group):
        if not group in self.groups:
            self.groups.append(group)
        return self.groups

    def add_permissions(self, perm):
        if not perm in self.permissions:
            self.permissions.append(perm)
        return self.permissions

    def has_perm(self, perm):
        return True if perm in self._permissions else False

    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        pass