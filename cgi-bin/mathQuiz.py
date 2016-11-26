#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response

def main():
	title = "title"
	body = """
		Link test<br>
		<a href="/cgi-bin/link.py">Link</a>
	"""
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
