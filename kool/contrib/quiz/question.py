from kool.db.models import Model


class Question(Model):
    """
    Question model provides a set of questions for a quiz.
    
    Extends:
        Model
    """
    def __init__(self, question, quiz_id, choices=[], **options):
        super().__init__()
        self.question = question
        self.quiz = quiz_id
        self.choices = choices
        self.answers = []

    def add_choice(self, choice):
        if not choice in self.choices:
            self.choices.append(choice)
        return self.choices

    def add_answer(self, answer):
        if not answer in self.answers:
            self.answers.append(answer)
        return self.answers


class Answer(Model):
    """
    These are answers to a question in a quiz.
    
    Extends:
        Model
    """

    def __init__(self, answer, question_id):
        super().__init__()
        self.answer = answer
        self.question_id = question_id
