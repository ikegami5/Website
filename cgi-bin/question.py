#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request

def main():
	br = "<br />"
	number = 1
	title = "Question No.{number}".format(number = str(number))
	body = """
		<form method="post" action="/cgi-bin/gameOver.py">
			1 + 1 = <input type="text" name="answer" />{br}
			<button type="submit" name="kakutei" value="kakutei">確定</button>{br}
		</form>
	""".format(br = br)
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
