#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request

def main():
	br = "<br />"
	number = 1
	title = "Question No.{number}".format(number = str(number))

	request = Request()
	name = request.data["name"].value

	body = """
		<form method="post" action="/cgi-bin/gameOver.py">
			<input type="hidden" name="name" value="{name}" />
			1 + 1 = <input type="text" name="answer" />{br}
			<button type="submit">確定</button>{br}
		</form>
	""".format(br = br, name = name)
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
