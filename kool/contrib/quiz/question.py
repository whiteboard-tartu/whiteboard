"""Question

This class represents questions that make up a quiz
"""

class Question(object):
	
	_questions = []

	def __init__(self, question, quiz):
		super().__init__()
		self.question = question
		self.quiz = quiz
		self.choices = {}
		self.answer = {}
		_questions.append(self)

	def questions(self):
		return self._questions

	def set_answer(self, answer):
		self.answer[self] = [answer]
		return self.answer

	def set_choices(self, choice):
		pass
		