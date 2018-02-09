import requests
from bs4 import BeautifulSoup

homepage = 'http://books.goalkicker.com/'

with requests.session() as s:

	home = s.get(homepage)
	bowl = BeautifulSoup(home.content, 'html.parser')

	for books in bowl.find_all('div', {'class': 'bookContainer grow'}):
		deepsearch = books.find_all('a')
		for i in deepsearch:

			book_url = homepage + i['href']

			# print(book_url)
