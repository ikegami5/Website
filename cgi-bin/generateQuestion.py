#!/usr/local/bin/python3
# coding: utf-8

from expression import Expression
from operators import Operator

class Question(object):
	pass

class IntQuestion(Question):

	def __init__(self):
		expression = self.generateExpression()
		self.expression = expression

	def generateExpression(self):
		return Expression(1, Operator.PLUS, 1)

	def answer(self):
		return self.expression.value()

	def __str__(self):
		str(self.expression)
