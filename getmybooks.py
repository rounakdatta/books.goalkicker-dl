import requests
from bs4 import BeautifulSoup

homepage = 'http://books.goalkicker.com/'

with requests.session() as s:

	home = s.get(homepage)
	bowl = BeautifulSoup(home.content, 'html.parser')

	# get the URLS for each book subpage from the homepage

	book_urls = []

	for books in bowl.find_all('div', {'class': 'bookContainer grow'}):
		deepsearch = books.find_all('a')

		for i in deepsearch:

			book_url = homepage + i['href']
			book_urls.append(book_url)

	# get book download link from each subpage and download it ;-)

	for book_front in book_urls:

		book_site = s.get(book_front)
		book_code = BeautifulSoup(book_site.content, 'html.parser')

		for dummy in book_code.find_all('div', {'id': 'frontpage'}):
			link_elem = dummy.findAll('a')

			for link in link_elem:

				download_payload = book_front + '/' + link['href']

				if('.pdf' in download_payload):
					download_link = download_payload

					print('Downloading ' + link['href'] + ' ...')

					file = s.get(download_link)
					with open(link['href'], 'wb') as f:
						f.write(file.content)