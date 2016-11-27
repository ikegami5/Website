#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response
import sys

def main():
	title = "Log in success!"
	br = "<br />"
	body = """
		Your data:
	""" + br
	body + "\t" + sys.stdin.read() + br
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
