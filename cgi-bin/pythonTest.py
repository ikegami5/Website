#!/usr/local/bin/python3
# coding: utf-8
import sys
from httpHandler import Response

def main():
	br = "</br>"
	title = "Python練習1"
	body = "Hello, Python!" + br
	version = list(sys.version_info)[0:3]
	body += "version: {0[0]}.{0[1]}.{0[2]}".format(version)
	body += br
	response = Response(title, body)
	response.respond()

if __name__ == "__main__":
	main()
