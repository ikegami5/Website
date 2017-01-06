#!/usr/local/bin/python3
# coding: utf-8
from httpHandler import Response, Request
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

	body = """
		<form method="post" action="{link}">
			<input type="hidden" name="name" value="{name}" />
			<input type="hidden" name="number" value="{number}" />
			<input type="hidden" name="score" value="{score}" />
			<input type="hidden" name="rightAnswer" value="{rightAnswer}" />
			{question} = <input type="text" name="answer" />{br}
			<button type="submit">確定</button>{br}
		</form>
	""".format(br = br, name = name, link = link, number = str(number + 1), 
		question = str(question), score = str(score), rightAnswer = str(question.answer()))
	res = Response(title, body)
	res.respond()

if __name__ == '__main__':
	main()
