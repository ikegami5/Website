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
		pass
	elif "password" not in data:
		pass
	else:
		body += """
			Your name: {name} {br}
			Your password: {password} {br}
		""".format(name = data[name].value, password = data[password].value, br = br)
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
