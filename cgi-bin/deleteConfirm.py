#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request
from htmlTemplate import Form

def main():
	request = Request()
	toDo = request.data["button"].value
	name = request.data["name"].value
	password = request.data["password"].value
	br = "<br />"
	title = ""
	body = ""

	formBody = """
		<button type="submit" name="button" value="yes">はい</button>
		<button type="submit" name="button" value="no">いいえ</button>
	"""
	form = None

	if toDo == "reset":
		title = "Reset score"
		body = "スコアをリセットします。よろしいですか？" + br
		form = Form("post", "/cgi-bin/delete.py", formBody, 
			("name", name), ("password", password), ("toDo", "reset"))
	elif toDo == "delete":
		title = "Delete account"
		body = "アカウントを消去します。よろしいですか？" + br
		form = Form("post", "/cgi-bin/delete.py", formBody, 
			("name", name), ("password", password), ("toDo", "delete"))
	body += str(form) + br
	res = Response(title, body)
	res.respond()

if __name__ == "__main__":
	main()
