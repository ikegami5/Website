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

class Form(object):
	def __init__(self, action, method = "post", body = "", *hiddenValues):
		self.html = """
			<form method="{method}" action="{action}">
				{hidden}
				{body}
			</form>
		""".format(method = method, action = action, body = body, hidden = "{hidden}")
		hiddenHtml = """
			<input type="hidden" name="{name}" value="{value}" />
			{hidden}
		"""
		hidden = "{hidden}"
		for hiddenValue in hiddenValues:
			hiddenHtmlFormat = hiddenHtml.format(name = hiddenValue[0], 
				value = hiddenValue[1], hidden = "{hidden}")
			hidden = hidden.format(hidden = hiddenHtmlFormat)
		self.html = self.html.format(hidden = hidden.format(hidden = ""))

	def __str__(self):
		return self.html
