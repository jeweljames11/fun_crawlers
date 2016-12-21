# hacker_news
# displays the latest x posts on the Hacker News website

import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/";
res = requests.get(url)

print("[Y][Hacker News]\n")
soup = BeautifulSoup(res.text,"html.parser")
links = soup.find_all("a", class_="storylink")
for index, link in enumerate(links):
	print(str(index+1) + ") " + link.get_text() + "\n" + link.get('href') + "\n")

