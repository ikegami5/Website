#!/usr/local/bin/python3
# coding: utf-8

import math
from fractions import Fraction
from operator.Operator import PLUS, MINUS, TIMES, DIVIDE

class Expression(object):

	def __init__(self, arg1, operator, arg2):
		if isinstance(arg1, Expression):
			self.arg1 = arg1
		else:
			self.arg1 = Fraction(arg1)
		self.operator = operator
		if isinstance(arg2, Expression):
			self.arg2 = arg2
		else:
			self.arg2 = Fraction(arg2)

	def value(self):
		if self.operator == PLUS:
			return self.arg1 + self.arg2
		elif self.operator == MINUS:
			return self.arg1 - self.arg2
		elif self.operator == TIMES:
			return self.arg1 * self.arg2
		elif self.operator == DIVIDE:
			return self.arg1 / self.arg2

	#def __add__(self, other):


	def __str__(self):
		if self.operator in [TIMES, DIVIDE]:
			if isinstance(self.arg1, Expression):
				if self.arg1.operator in [PLUS, MINUS]:
					expr1 = "( " + str(self.arg1) + " ) "
			if isinstance(self.arg2, Expression):
				if self.arg2.operator in [PLUS, MINUS]:
					expr2 = " ( " + str(self.arg2) + " )"
		return expr1 + self.operator.value() + expr2

if __name__ == '__main__':
	a = Expression(3, PLUS, 5)
	b = Expression(4, MINUS, 2)
	c = Expression(a, TIMES, b)
	print(c) # ( 3 + 5 ) × ( 4 - 2 )
	print(c.value()) #16
