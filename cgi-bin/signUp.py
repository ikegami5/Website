#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request

def main():
	request = Request()
	error = request.data["error"].value
	errorMessage = ""
	br = "<br />"
	if error == "noName":
		errorMessage += '<div class="error">Input your name.</div>' + br
	elif error == "noPass":
		errorMessage += '<div class="error">Input your password.</div>' + br
	elif error == "alreadyExist":
		errorMessage += '<div class="error">That name already exists.</div>' + br
	title = "Sign Up"
	body = """
		{errorMessage}
		<form method="post" action="/cgi-bin/link.py">
			Name: <input type="text" name="name" />{br}
			Password: <input type="password" name="password" />{br}
			<input type="submit" name="submit" value="Log in" />{br}
		</form>
	""".format(errorMessage = errorMessage, br = br)
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
