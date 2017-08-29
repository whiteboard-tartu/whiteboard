"""
Answer

This class represents answers to a question
"""
from kool.db.models import Model


class Answer(Model):

	_answers = []

	def __init__(self, student, answer):
		super().__init__()
		self.student = student
		self.answer = answer

