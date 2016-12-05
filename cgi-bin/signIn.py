#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request

def main():
	br = "<br />"
	title = "Sign In"
	request = Request()
	error = request.data["error"].value
	errorMessage = ""
	if error == "noName":
		errorMessage += '<div class="error">Input your name.</div>' + br
	elif error == "noPass":
		errorMessage += '<div class="error">Input your password.</div>' + br
	elif error == "doNotExist":
		errorMessage += '<div class="error">That name does not exist.</div>' + br
	elif error == "wrongPass":
		errorMessage += '<div class="error">That password is wrong.</div>' + br
	body = """
		{errorMessage}
		<form method="post" action="/cgi-bin/signInSuccess.py">
			Name: <input type="text" name="name" />{br}
			Password: <input type="password" name="password" />{br}
			<button type="submit" name="submit" value="signIn">Sign in</button>{br}
		</form>
	""".format(errorMessage = errorMessage, br = br)
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
