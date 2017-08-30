from kool.db.models import Model


class Quiz(Model):
    """
    Quiz class
    """

    def __init__(self, name, course_id, **options):
        super().__init__()
        self.name = name
        self.course_id = course_id
        self.description = options.pop('description', None)


        
