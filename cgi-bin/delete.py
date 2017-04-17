#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request
import MySQLdb
from dbPass import dbName, dbPass
from htmlTemplate import DBExpression, Form
from myError import DBError

def main():
	try:
		dbConnector = MySQLdb.connect(
				user = dbName,
				passwd = dbPass,
				host = "localhost",
				db = "mathQuizUsers"
			)
		dbCursor = dbConnector.cursor()

		request = Request()
		data = request.data
		toDo = data["toDo"].value
		name = data["name"].value
		password = data["password"].value
		button = data["button"].value
		form = None

		if toDo == "reset":
			if button == "yes":
				pass
			elif button == "no":
				form = Form("post", "/cgi-bin/signInSuccess.py", "", 
					("name", name), ("password", password))
		elif toDo == "delete":
			if button == "yes":
				pass
			elif button == "no":
				form = Form("post", "/cgi-bin/signInSuccess.py", "", 
					("name", name), ("password", password))

	finally:
		dbCursor.close()
		dbConnector.close()

if __name__ == "__main__":
	main()
