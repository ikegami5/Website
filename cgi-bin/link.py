#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response

def main():
	title = "title"
	br = "<br />"
	body = """
		Data
	""" + br
	while True:
		try:
			body + input() + br
		except EOFError:
			break
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
