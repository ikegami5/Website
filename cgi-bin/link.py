#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request
import MySQLdb
from dbPass import dbName, dbPass
from htmlTemplate import DBExpression

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
		print("Location: /cgi-bin/mathQuiz.py?error=noName\n")
	elif "password" not in data:
		print("Location: /cgi-bin/mathQuiz.py?error=noPass\n")
	else:
		name = data["name"].value
		password = data["password"].value
		dbCursor.execute('SELECT * FROM users WHERE name = "{name}"'.format(name = name))

		body += str(dbCursor.fetchall());

		if (True):

			body += """
				Your name: {name} {br}
				Your password: {password} {br}
			""".format(name = name, password = password, br = br)

			dbData = DBExpression("Name", "Password")
			dbCursor.execute("SELECT * FROM users")
			for row in dbCursor.fetchall():
				dbData.appendData(*row)
			body += str(dbData) + br

			res = Response(title, body)
			res.respond()

	dbCursor.close()
	dbConnector.close()

if __name__ == "__main__":
	main()
