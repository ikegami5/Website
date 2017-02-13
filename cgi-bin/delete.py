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
		toDo = request.data.getValue("button")
		title = ""
		body = ""
		if toDo == "reset":
			title = "Reset score"
			body = "スコアをリセットします。よろしいですか？"
		elif toDo == "delete":
			title = "Delete account"
			body = "アカウントを消去します。よろしいですか？"
		res = Response(title, body)
		res.respond()
	finally:
		dbCursor.close()
		dbConnector.close()

if __name__ == "__main__":
	main()
