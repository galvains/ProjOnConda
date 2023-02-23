import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\
    605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'
}

# list_card_url = []

def download(url):
    resp = requests.get(url, stream=True)
    with open('/Users/yarik/Desktop/data/' + url.split('/')[-1], 'wb') as file:
        for value in resp.iter_content(1024 ** 2):
            file.write(value)


def parse():
    for page in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')


        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

        for i in data:

            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url

            # name = i.find('h4', class_='card-title').text.strip()
            # price = i.find('h5').text.strip()
            # url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
            # print(f'{name} {price}\n{url_img}\n')

def func():
    for card_url in parse():
        response = requests.get(card_url, headers=headers)
        sleep(2)
        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find('div', class_='card mt-4 my-4')
        name = data.find('h3', class_='card-title').text
        price = data.find('h4').text
        card_text = data.find('p', class_='card-text').text
        url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
        download(url_img)
        yield name, price, card_text, url_img