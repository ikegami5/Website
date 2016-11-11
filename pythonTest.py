#!/bin/env python3
# coding: utf-8
import sys

def main():
	br = "</br>"
	print("Content-type: text/html\n")
	html = "<html><body>{0}</body></html>"
	body = "Hello, Python!" + br
	version = list(sys.version_info)[0:3]
	body += "version: {0[0]}.{0[1]}.{0[2]}".format(version)
	body += br
	print(html.format(body))

if __name__ == "__main__":
	main()

