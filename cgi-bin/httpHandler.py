#!/usr/local/bin/python3
# coding: utf-8
import cgi

class Response(object):
	def __init__(self, title, body):
		self.html = """
			<!DOCTYPE html>
			<html lang="ja">
			<head>
				<meta charset="UTF-8" />
				<title>{title}</title>
				<link rel="stylesheet" type="text/css" href="/style.css" />
			</head>
			<body>
				<h1>{title}</h1>
				<p>{body}</p>
				<h2>Link</h2>
				<a href="/index.html">TOP</a>
			</body>
			</html>
		"""
		self.title = title
		self.body = body
		self.html = self.html.format(title = self.title, body = self.body)

	def respond(self):
		print("Content-type: text/html\n")
		print(self.html)

class Request(object):
	def __init__(self):
		self.data = cgi.FieldStorage()
		