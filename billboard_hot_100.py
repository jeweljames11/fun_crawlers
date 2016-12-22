# billboard_hot_100
# displays the Billboard Hot 100 chart

import requests
from bs4 import BeautifulSoup

# I don't know why there's a dozen or so spaces before the link text,
# anyway here's the recipe to remove 'em
def remove_spaces(string):
	# leading spaces
	index = 0
	for i in range(0,len(string)):
		if not string[i].isspace():
			index = i
			break
	if index != 0:
		string = string[i:]
	# trailing spaces
	for i in range(0,len(string)):
		if string[i:].isspace():
			string = string[:i]
	return string

print("Billboard Hot 100")
url = "http://www.billboard.com/charts/hot-100";
res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")
blocks = soup.find_all("div", class_="chart-row__title")
index = 1
for block in blocks:
	song = block.find(class_='chart-row__song').get_text()
	artist = block.find(class_='chart-row__artist').get_text()
	artist = remove_spaces(artist)
	print(str(index) + ") " + song + " - " + artist)
	index += 1


	