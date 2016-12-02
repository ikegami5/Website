#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response

def main():
	br = "<br />"
	title = "Math Quiz"
	body = """
		<form method="get" action="/cgi-bin/signUp.py?error=none>
			<button type="button" value="Sign up" />
		</form>
		<form method="get" action="/cgi-bin/signIn.py?error=none>
			<button type="button" value="Sign in" />
		</form>
	"""
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
