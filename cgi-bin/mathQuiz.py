#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response

def main():
	title = "Log in"
	body = """
		Post test<br>
		<form method="post" action="/cgi-bin/link.py">
			Name: <input type="text" name="name" />
			Password: <input type="password" name="password" />
		</form>
	"""
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
