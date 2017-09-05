from kool.core.exceptions import UserNotFound, PermissionNotFound
from kool.db.models import Model, where, table
from kool.contrib.auth.hasher import make_password, check_password
from .group import Group
from .permission import Permission


class User(Model):
    """Base class for users"""
    
    def __init__(self, * args, **kwargs):
        super().__init__()
        self.email = kwargs['email']
        self.password = self.set_password(kwargs['password'])
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.is_active = True
        self.groups = []
        self.permissions = []

    def __str__(self):
        return '{}'.format(self.full_name())

    def __repr__(self):
        return '{}'.format(self.full_name())

    def set_password(self, raw_password):
        """
        Return encoded password
        
        Arguments:
            raw_password {str} -- users raw password
        
        Returns:
            [str] -- encoded password
        """
        return make_password(raw_password)

    def check_password(self, raw_password):
        """
        Checks if the password matches correctly
        
        Arguments:
            raw_password {str} -- users raw password
        
        Returns:
            [bool] -- return True if users password matches
        """
        def setter(raw_password):
            self.set_password(raw_password)

        return check_password(raw_password, self.password, setter) 

    def add_group(self, group_id):
        """
        Adds user to multiple groups.
        
        Arguments:
            group_id {str} -- a group id
        
        Returns:
            list -- a list of group id's
        
        Raises:
            ValueError -- Group id not found!
        """
        group = table(Group)

        if group.get(where('_id') == str(group_id)):
            if not group_id in self.groups:
                self.groups.append(group_id)
        else:
            raise ValueError('Group id not found!')

        self.update()

        return self.groups

    def del_group(self, group_id):
        """
        Receives a group id and deletes it from 
        a list of group ids for a given user
        """
        if group_id in self.groups:
            self.groups.remove(group_id)
        
        self.update()

        return self.groups

    def add_permission(self, perm_id):
        """
        Assigns user multiple permissions
        
        Arguments:
            perm_id {str} -- a permission id
        
        Returns:
            list -- a list of permissions id's
        
        Raises:
            ValueError -- Permission id not found!
        """
        permission = table(Permission)

        if permission.get(where('_id') == str(perm_id)):
            if not perm_id in self.permissions:
                self.permissions.append(perm_id)
        else:
            raise ValueError('Permission id not found!')

        self.update()

        return self.permissions

    def del_permission(self, perm_id):
        """
        Receives a permission id and deletes it from 
        a list of permission ids for a given user
        """
        if perm_id in self.permissions:
            self.permissions.remove(perm_id)
        
        self.update()

        return self.permissions

    def has_perm(self, perm_id):
        """Checks if a user has a given permission"""
        permission = table(Permission)
        
        if permission.get(where('_id') == str(perm_id)):
            return True
        else:
            raise PermissionNotFound

    def full_name(self):
        """Returns users full name"""
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        pass