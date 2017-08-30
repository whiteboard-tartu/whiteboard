from kool.db.models import Model


class Topic(Model):
    """
    These are topics that constitute a course
    
    Extends:
        Model
    """

    def __init__(self, title, **options):
        super().__init__()
        self.title = title
        self.description = options.pop('description', None)
        self.file_id = options.pop('file_id', None)


class Course(Model):
    """
    Course describes a plan of study for a student
    
    Extends:
        Model
    """
    
    def __init__(self, title, instructor_id, **options):
        super().__init__()
        self.title = title
        self.instructor_id = instructor_id
        self.description = options.pop('description', None)
        self.topics = []

    def add_topic(self, topic_id):
        if not topic_id in self.topics:
            self.topics.append(topic_id)
        return self.topics

    def del_topic(self, topic_id):
        if topic_id in self.topics:
            self.topics.remove(topic_id)
        return self.topics
