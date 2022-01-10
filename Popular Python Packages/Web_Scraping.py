import requests
from bs4 import BeautifulSoup

reponse = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(reponse.text, "html.parser")

questions = soup.select(".question-summary")
# print(questions[0].get("id", 0))# getting attribute
# print(questions[0].select(".question-hyperlink")) # returns a list
# print(questions[0].select_one(".question-hyperlink"))  # returns single object
for question in questions:
    print(question.select_one(".question-hyperlink").get_text())
    print(question.select_one(".vote-count-post").get_text())
