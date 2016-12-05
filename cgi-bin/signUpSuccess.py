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
	errorLoc = "Location: /cgi-bin/signUp.py?error={error}\n"
	if "name" not in data:
		print(errorLoc.format(error = "noName"))
	elif "password" not in data:
		print(errorLoc.format(error = "noPass"))
	else:
		name = data["name"].value
		password = data["password"].value
		dbCursor.execute('SELECT * FROM users WHERE name = "{name}"'.format(name = name))

		if dbCursor.fetchall() != ():
			print(errorLoc.format(error = "alreadyExist"))
		else:
			dbCursor.execute("""
				INSERT INTO users 
				VALUES ("{name}", "{password}")
			""".format(name = name, password = password))
			dbConnector.commit()

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
