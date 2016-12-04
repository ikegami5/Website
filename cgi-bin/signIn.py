#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request

def main():
	br = "<br />"
	title = "Sign In"
	body = ""
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
