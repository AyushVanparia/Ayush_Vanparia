import requests
from bs4 import BeautifulSoup

reponse = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(reponse.text, "html.parser")

questions = soup.select(".question-summary")
print(questions[0].get("id", 0))
