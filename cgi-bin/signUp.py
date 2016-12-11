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
		<div class="caution">
			<div class="thick">注意!</div>
			セキュリティがガバガバなので、他のサイトで使用しているパスワードは<br />
			絶対に入力しないでください！
		</div>
		{errorMessage}
		<form method="post" action="/cgi-bin/signUpSuccess.py">
			Name: <input type="text" name="name" />{br}
			Password: <input type="password" name="password" />{br}
			<button type="submit" name="submit" value="signUp">Sign up</button>{br}
		</form>
	""".format(errorMessage = errorMessage, br = br)
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
