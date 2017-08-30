from kool.db.models import Model, where
from .question import Question, Answer


class Quiz(Model):
    """
    Quiz comprises of questions and answers
    """

    def __init__(self, name, course_id, **options):
        super().__init__()
        self.name = name
        self.course_id = course_id
        self.student_id = options.pop('student_id', None)
        self.description = options.pop('description', None)

    def add_question(self, question, choices=None):
        """Adds a question to this quiz if it exists in db"""
        if self._id:
            q = Question(question, self._id, choices=choices)
            q.save()
        else:
            raise ValueError('Quiz must be saved to add a question!')

    def questions(self):
        """Returns a list of all questions related to quiz"""
        questions = []
        if self._id:
            q = Question(None, self._id)  # instantiate empty question
            questions = q.filter(where('_id') == str(self._id))
        return questions
