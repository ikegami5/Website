#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request

def main():
	request = Request()
	answer = int(request.data["answer"].value)
	if answer == 2:
		score = 1
	else:
		score = 0
	br = "<br />"
	title = "Game Over"
	body = """
		score = {score}{br}
	""".format(br = br, score = score)
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
