from kool.db.models import Model


class Permission(Model):
    """
    Permissions are used to determine actions permitted on a course
    by a user or group

    Extends:
        Model
    """
    
    def __init__(self, name, course_id, codename=None):
        super().__init__()
        self.name = name
        self.course_id = course_id
        self.codename = codename if codename else str(self.name).lower()
