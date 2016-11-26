#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response

def main():
	title = "title"
	body = """
		Link<br>
	"""
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
