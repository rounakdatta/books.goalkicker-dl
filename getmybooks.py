import requests
from bs4 import BeautifulSoup

homepage = 'http://books.goalkicker.com/'

with requests.session() as s:

	home = s.get(homepage)
	bowl = BeautifulSoup(home.content, 'html.parser')

	book_urls = []

	for books in bowl.find_all('div', {'class': 'bookContainer grow'}):
		deepsearch = books.find_all('a')

		for i in deepsearch:

			book_url = homepage + i['href']
			book_urls.append(book_url)

			# print(book_url)
	
	# print(book_urls)

	for book_front in book_urls:

		book_site = s.get(book_front)
		book_code = BeautifulSoup(book_site.content, 'html.parser')

		for dummy in book_code.find_all('div', {'id': 'frontpage'}):
			link_elem = dummy.findAll('a')

			for link in link_elem:

				download_link = book_front + '/' + link['href']

				print(download_link)