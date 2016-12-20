#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request

def main():
	br = "<br />"
	title = "Game Over"
	body = """
		gameover{br}
	""".format(br = br)
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
