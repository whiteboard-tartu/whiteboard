from kool.db.models import Model


class Question(Model):
	
	def __init__(self, question, quiz_id):
		super().__init__()
		self.question = question
		self.quiz = quiz_id
		self.choices = {}
		self.answer = {}

	def questions(self):
		return self._questions

	def set_answer(self, answer):
		self.answer[self] = [answer]
		return self.answer

	def set_choices(self, choice):
		pass


class Answer(Model):

	_answers = []

	def __init__(self, student, answer):
		super().__init__()
		self.student = student
		self.answer = answer		