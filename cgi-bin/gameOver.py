#!/usr/local/bin/python3
# coding: utf-8
import MySQLdb
from httpHandler import Response, Request

def main():
	br = "<br />"
	title = "Game Over"

	dbConnector = MySQLdb.connect(
		user = dbName,
		passwd = dbPass,
		host = "localhost",
		db = "mathQuizUsers"
	)
	dbCursor = dbConnector.cursor()

	request = Request()
	answer = int(request.data["answer"].value)
	if answer == 2:
		score = 1
	else:
		score = 0
	name = request.data["name"].value

	dbCursor.execute("""
		UPDATE users SET {score} WHERE name = {name}
	""".format(name = name, score = score))
	dbConnector.commit()

	dbData = DBExpression("Name", "Score")
	dbCursor.execute("SELECT * FROM users")
	for row in dbCursor.fetchall():
		dbData.appendData(row[0], str(row[2]))

	body = """
		score = {score}{br}
	""".format(br = br, score = score)
	body += str(dbData) + br
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
