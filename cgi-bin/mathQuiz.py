#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response

def main():
	br = "<br />"
	title = "Math Quiz"
	body = """
		<form method="get" action="/cgi-bin/signUp.py?error=none>
			<button type="submit" value="signUp" name="action">Sign up</button>
		</form>
		<form method="get" action="/cgi-bin/signIn.py?error=none>
			<button type="submit" value="signIn" name="action">Sign in</button>
		</form>
	"""
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
