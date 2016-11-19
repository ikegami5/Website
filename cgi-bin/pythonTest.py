#!/usr/local/bin/python3
# coding: utf-8
import sys

import io

def main():
	br = "</br>"
	print("Content-type: text/html\n")
	html = """
		<!DOCTYPE html>
		<html lang="ja">
		<head>
			<meta charset="UTF-8" />
			<title>Python練習1</title>
			<link rel="stylesheet" type="text/css" href="../html/style.css" />
		</head>
		<body>
			<h1>Python練習1</h1>
			<p>{0}</p>
			<p>{1}</p>
			<h2>Link</h2>
			<a href="./index.html">TOP</a>
		</body>
		</html>
	"""
	body = "Hello, Python!" + br
	version = list(sys.version_info)[0:3]
	body += "version: {0[0]}.{0[1]}.{0[2]}".format(version)
	body += br
	debug = sys.stdout.encoding
	print(html.format(body, debug))

if __name__ == "__main__":

	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

	main()

