#!/usr/local/bin/python3
# coding: utf-8
import MySQLdb
from httpHandler import Response, Request
from dbPass import dbName, dbPass
from htmlTemplate import DBExpression

def main():
	br = "<br />"
	title = "Game Over"

	try:
		dbConnector = MySQLdb.connect(
			user = dbName,
			passwd = dbPass,
			host = "localhost",
			db = "mathQuizUsers"
		)
		dbCursor = dbConnector.cursor()

		request = Request()
		score = int(request.data["score"].value)
		answer = request.data["answer"].value
		rightAnswer = request.data["rightAnswer"].value
		if rightAnswer == answer:
			score = score + 1
		name = request.data["name"].value

		dbCursor.execute("""
			SELECT * FROM users WHERE name = "{name}"
		""".format(name = name))
		if score > dbCursor.fetchone()[2]:
			dbCursor.execute("""
				UPDATE users SET score = {score} WHERE name = "{name}"
			""".format(name = name, score = str(score)))
			dbConnector.commit()

		dbData = DBExpression("Name", "Score")
		dbCursor.execute("SELECT * FROM users")
		for row in dbCursor.fetchall():
			dbData.appendData(row[0], str(row[2]))

		body = """
			score = {score}{br}
		""".format(br = br, score = str(score))
		body += str(dbData) + br
		res = Response(title, body)
		res.respond()
	finally:
		dbCursor.close()
		dbConnector.close()

if __name__ == '__main__':
	main()
