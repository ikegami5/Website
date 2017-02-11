#!/usr/local/bin/python3
# coding: utf-8

from expression import Expression
from operators import Operator
import random

class Question(object):
	pass

class IntQuestion(Question):

	def __init__(self):
		self.expression = self.generateExpression()

	def generateExpression(self):

		def value(expr):
			if isinstance(expr, Expression):
				return expr.value()
			else:
				return expr

		def areAllowedPlus(expr1, expr2):
			value1 = value(expr1)
			value2 = value(expr2)
			if value1 + value2 > 200:
				return False
			if value1 + value2 < -200:
				return False
			return True

		def areAllowedMinus(expr1, expr2):
			value1 = value(expr1)
			value2 = value(expr2)
			if abs(value1 - value2) > 200:
				return False
			else:
				return True

		def areAllowedTimes(expr1, expr2):
			absValue1 = abs(value(expr1))
			absValue2 = abs(value(expr2))
			if absValue1 * absValue2 > 200:
				return False
			if absValue1 < 2 or absValue2 < 2:
				return False
			return True

		def areAllowedDivide(expr1, expr2):
			absValue1 = abs(value(expr1))
			absValue2 = abs(value(expr2))
			if absValue1 < 2 or absValue2 < 2:
				return False
			else:
				if absValue1 % absValue2 == 0 and absValue1 / absValue2 != 1:
					return True
				elif absValue2 % absValue1 == 0 and absValue2 / absValue1 != 1:
					return True
				else:
					return False

		def uniteExprs(expr1, operator, expr2):
			if operator in [Operator.PLUS, Operator.MINUS, Operator.TIMES]:
				return Expression(expr1, operator, expr2)
			else:
				if abs(value(expr1)) % abs(value(expr2)) == 0:
					return Expression(expr1, operator, expr2)
				else:
					return Expression(expr2, operator, expr1)

		numberCount = random.randint(3, 5)
		numbers = []
		for i in range(2, 10):
			for j in range(100):
				numbers.append(i)
		for i in range(-9, -1):
			for j in range(100):
				numbers.append(i)
		for i in range(10, 50):
			for j in range(10):
				numbers.append(i)
		for i in range(-49, -9):
			for j in range(10):
				numbers.append(i)
		for i in range(50, 200):
			numbers.append(i)
		for i in range(-199, -49):
			numbers.append(i)			
		exprs = [random.choice(numbers) for i in range(numberCount)]
		for i in range(numberCount - 1):
			position = random.randrange(0, len(exprs) - 1)
			expr1 = exprs[position]
			expr2 = exprs[position + 1]
			operators = []
			if areAllowedPlus(expr1, expr2):
				operators.append(Operator.PLUS)
			if areAllowedMinus(expr1, expr2):
				operators.append(Operator.MINUS)
			if areAllowedTimes(expr1, expr2):
				for j in range(8):
					operators.append(Operator.TIMES)
			if areAllowedDivide(expr1, expr2):
				for j in range(8):
					operators.append(Operator.DIVIDE)
			operator = random.choice(operators)
			newExpr = uniteExprs(expr1, operator, expr2)
			exprs[position : position + 2] = [newExpr]
		return exprs[0]

	def answer(self):
		return self.expression.value()

	def __str__(self):
		return str(self.expression)
