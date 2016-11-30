#!/usr/local/bin/python3
# coding: utf-8

class DBExpression(object):
	def __init__(self, *theme):
		self.html = """
			<table>
				<tr>
					{theme}
				</tr>
				{data}
			</table>
		"""
		for th in theme:
			self.html = self.html.format(theme = "<th>" + th + "</th>{theme}", data = "{data}")
		self.html = self.html.format(theme = "", data = "{data}")

	def appendData(self, *data):
		self.html = self.html.format(data = "<tr>{d}</tr>{data}")
		for d in data:
			self.html = self.html.format(d = "<td>" + d + "</td>{d}", data = "{data}")
		self.html = self.html.format(d = "", data = "{data}")

	def __str__(self):
		self.html = self.html.format(data = "")
		return self.html
