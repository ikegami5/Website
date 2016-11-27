#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request

def main():
	request = Request()
	data = request.data
	title = "Log in success!"
	br = "<br />"
	body = ""
	if "name" not in data:
		print("Location: /cgi-bin/mathQuiz.py?error=true\n")
	elif "password" not in data:
		print("Location: /cgi-bin/mathQuiz.py?error=true\n")
	else:
		body += """
			Your name: {name} {br}
			Your password: {password} {br}
		""".format(name = data["name"].value, password = data["password"].value, br = br)
		res = Response(title, body)
		res.respond()

if __name__ == "__main__":
	main()
