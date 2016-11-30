#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request
import MySQLdb
from dbPass import dbName, dbPass
from htmlTemplete import DBExpression

def main():
	dbConnector = MySQLdb.connect(
			user = dbName,
			passwd = dbPass,
			host = "localhost",
			db = "mathQuizUsers"
		)
	dbCursor = dbConnector.cursor()

	request = Request()
	data = request.data
	title = "Log in success!"
	br = "<br />"
	body = ""
	if "name" not in data:
		print("Location: /cgi-bin/mathQuiz.py?error=true\n")
	elif "password" not in data:
		print("Location: /cgi-bin/mathQuiz.py?error=true\n")
	else:
		dbData = DBExpression("Name", "Password")
		dbCursor.execute("SELECT * FROM users")
		for row in dbCursor.fetchall():
			dbData.appendData(*row)

		body += """
			Your name: {name} {br}
			Your password: {password} {br}
		""".format(name = data["name"].value, password = data["password"].value, br = br)

		body += str(dbData) + br

		res = Response(title, body)
		res.respond()

	dbCursor.close
	dbConnector.close

if __name__ == "__main__":
	main()
