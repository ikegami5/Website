#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response

def main():
	br = "<br />"
	title = "Math Quiz"
	body = """
		<button type="button" onclick="location.href='/cgi-bin/signUp.py?error=none'">
			Sign up
		</button>
		<button type="button" onclick="location.href='/cgi-bin/signIn.py?error=none'">
			Sign in
		</button>
	"""
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
