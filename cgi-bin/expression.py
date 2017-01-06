#!/usr/local/bin/python3
# coding: utf-8

import math
from fractions import Fraction
from operators import Operator

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
		if self.operator == Operator.PLUS:
			return self.arg1 + self.arg2
		elif self.operator == Operator.MINUS:
			return self.arg1 - self.arg2
		elif self.operator == Operator.TIMES:
			return self.arg1 * self.arg2
		elif self.operator == Operator.DIVIDE:
			return self.arg1 / self.arg2

	def __add__(self, other):
		if isinstance(other, Expression):
			return self.value() + other.value()
		elif isinstance(other, Fraction):
			return self.value() + other
		else:
			return NotImplemented

	def __sub__(self, other):
		if isinstance(other, Expression):
			return self.value() - other.value()
		elif isinstance(other, Fraction):
			return self.value() - other
		else:
			return NotImplemented

	def __mul__(self, other):
		if isinstance(other, Expression):
			return self.value() * other.value()
		elif isinstance(other, Fraction):
			return self.value() * other
		else:
			return NotImplemented

	def __truediv__(self, other):
		if isinstance(other, Expression):
			return self.value() / other.value()
		elif isinstance(other, Fraction):
			return self.value() / other
		else:
			return NotImplemented

	def __str__(self):
		expr1 = str(self.arg1) + " "
		expr2 = " " + str(self.arg2)
		if self.operator in [Operator.TIMES, Operator.DIVIDE]:
			if isinstance(self.arg1, Expression):
				if self.arg1.operator in [Operator.PLUS, Operator.MINUS]:
					expr1 = "( " + str(self.arg1) + " ) "
			if isinstance(self.arg2, Expression):
				if self.arg2.operator in [Operator.PLUS, Operator.MINUS]:
					expr2 = " ( " + str(self.arg2) + " )"
		return expr1 + self.operator.value + expr2

if __name__ == '__main__':
	a = Expression(3, Operator.PLUS, 5)
	b = Expression(4, Operator.MINUS, 2)
	c = Expression(a, Operator.TIMES, b)
	print(c) # ( 3 + 5 ) × ( 4 - 2 )
	print(c.value()) # 16
