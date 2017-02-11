#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request
from htmlTemplate import Form
from generateQuestion import IntQuestion

def main():
	br = "<br />"
	request = Request()
	name = request.data["name"].value
	number = int(request.data["number"].value)
	score = int(request.data["score"].value)
	if number != 1:
		answer = request.data["answer"].value
		rightAnswer = request.data["rightAnswer"].value
		if rightAnswer == answer:
			score = score + 1
	title = "Question No.{number}".format(number = str(number))

	if number == 2:
		link = "/cgi-bin/gameOver.py"
	else:
		link = "/cgi-bin/question.py"
	question = IntQuestion()

	hidden = [("name", name), ("number", str(number + 1)), ("score", str(score)), 
		("rightAnswer", str(question.answer()))]
	formBody = """
		{question} = <input type="text" name="answer" />{br}
		<button type="submit">確定</button>{br}
	""".format(question = str(question), br = br)
	form = Form("post", link, formBody, *hidden)

	body = str(form)
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
