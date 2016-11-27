#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response

def main():
	title = "Log in"
	br = "<br />"
	body = """
		Post test{br}
		<form method="post" action="/cgi-bin/link.py">
			Name: <input type="text" name="name" />{br}
			Password: <input type="password" name="password" />{br}
			<input type="submit" name="submit" value="Log in" />{br}
		</form>
	""".format(br = br)
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
