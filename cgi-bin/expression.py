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

	def __radd__(self, other):
		return self.__add__(other)

	def __rsub__(self, other):
		return other - self.value()

	def __rmul__(self, other):
		return self.__mul__(other)

	def __rtruediv__(self, other):
		return other / self.value()

	def __str__(self):
		if isinstance(self.arg1, Fraction):
			if self.arg1 < 0:
				expr1 = "(" + str(self.arg1) + ") "
			else:
				expr1 = str(self.arg1) + " "
		if isinstance(self.arg2, Fraction):
			if self.arg2 < 0:
				expr2 = " (" + str(self.arg2) + ")"
			else:
				expr2 = " " + str(self.arg2)
		if isinstance(self.arg1, Expression):
			if self.operator in [Operator.TIMES, Operator.DIVIDE]:
				if self.arg1.operator in [Operator.PLUS, Operator.MINUS]:
					expr1 = "(" + str(self.arg1) + ") "
		if isinstance(self.arg2, Expression):
			if self.operator in [Operator.TIMES, Operator.MINUS]:
				if self.arg2.operator in [Operator.PLUS, Operator.MINUS]:
					expr2 = " (" + str(self.arg2) + ")"
			elif self.operator == Operator.DIVIDE:
				expr2 = " (" + str(self.arg2) + ")"
		return expr1 + self.operator.value + expr2
