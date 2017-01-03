#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request
import MySQLdb
from dbPass import dbName, dbPass
from htmlTemplate import DBExpression
from myError import DBError

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
	title = "Sign in success!"
	br = "<br />"
	body = ""
	errorLoc = "Location: /cgi-bin/signIn.py?error={error}\n"
	if "name" not in data:
		print(errorLoc.format(error = "noName"))
	elif "password" not in data:
		print(errorLoc.format(error = "noPass"))
	else:
		name = data["name"].value
		password = data["password"].value
		dbCursor.execute('SELECT * FROM users WHERE name = "{name}"'.format(name = name))
		users = dbCursor.fetchall()

		if users == ():
			print(errorLoc.format(error = "doNotExist"))
		elif len(users) >= 2:
			raise DBError()
		else:
			if users[0][1] != password:
				print(errorLoc.format(error = "wrongPass"))
			else:
				dbData = DBExpression("Name", "Score")
				dbCursor.execute("SELECT * FROM users")
				for row in dbCursor.fetchall():
					dbData.appendData(row[0], str(row[2]))

				body += """
					<form method="post" action="/cgi-bin/question.py">
						<button type="submit">Start!</button>
						<input type="hidden" name="name" value="{name}" />
					</form>
				"""
				body += str(dbData) + br

				res = Response(title, body)
				res.respond()

	dbCursor.close()
	dbConnector.close()

if __name__ == "__main__":
	main()
