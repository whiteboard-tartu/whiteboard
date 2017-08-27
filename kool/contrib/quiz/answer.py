"""Answer

This class represents answers to a question
"""

class Answer(object):

	_answers = []

	def __init__(self, student, answer):
		super().__init__()
		self.student = student
		self.answer = answer

