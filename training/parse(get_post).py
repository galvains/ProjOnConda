import requests
from requests import Session
from bs4 import BeautifulSoup


headers = {
	'User-Agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\
    605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'
}

# for page in range(1, 11):
#
#     url = f'https://quotes.toscrape.com/page/{page}'
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'lxml')
#
#     data = soup.find_all('div', class_='quote')
#     for card in data:
#         txt_card = card.find('span', class_='text').text
#         author = card.find('small', class_='author').text
#         print(f'\n{txt_card} by {author}')
#
#         tags = card.find_all('a', class_='tag')
#         for tag in tags:
#             name_tag = tag.text
#             print(name_tag, end=' ')

work = Session()

data = {
    'csrf_token': '',
    'username': 'yarik',
    'password': '1111'
}

post_url = 'https://quotes.toscrape.com/login'
post_response = work.get(post_url, headers=headers)
post_soup = BeautifulSoup(post_response.text, 'lxml')

token = post_soup.find('input').get('value')

data = {
    'csrf_token': token,
    'username': 'yarik',
    'password': '1111'
}

POST = work.post(post_url, data=data, headers=headers, allow_redirects=True)

print(POST.text)
