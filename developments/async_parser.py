import requests
import json
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from time import time

start_time = time()

async def get_page_data(session, page, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\
        605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'
    }
    url = f'https://www.labirint.ru/genres/2304/?page={page}'

    async with session.get(url, headers=headers) as response:
        response_text = await response.text()

        soup = BeautifulSoup(response_text, 'lxml')
        cards = soup.find('div', class_='genres-catalog').find_all('div', class_="genres-carousel__item")

        with open('parse_data_async.json', 'w') as file:
            for card in cards:
                price = card.find('span', class_='price-val').text.strip()
                name = card.find('a', class_='product-title-link').get('title')

                data['items'].append({'name': name, 'price': price})

            json.dump(data, file, indent=4, ensure_ascii=False)
    print(f'[+] Complete {page} page')


async def gather_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\
        605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'
    }
    url = 'https://www.labirint.ru/genres/2304/'

    data = {}
    data['items'] = []

    async with aiohttp.ClientSession() as session:
        tasks = []

        response = await session.get(url, headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')

        pagination = int(soup.find('div', class_='pagination-number__right').find \
                                    ('a', class_='pagination-number__text').text)

        for page in range(1, pagination + 1):
            task = asyncio.create_task(get_page_data(session, page, data))
            tasks.append(task)
        await asyncio.gather(*tasks)


def main():
    asyncio.run(gather_data())
    finish_time = time() - start_time
    print(f'Total time: {round(finish_time, 2)} sec.')


'''
start_time = time()

def get_data(url, data):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find('div', class_='genres-catalog').find_all('div', class_="genres-carousel__item")

    with open('parse_data.json', 'w') as file:

        for card in cards:
            price = card.find('span', class_='price-val').text.strip()
            name = card.find('a', class_='product-title-link').get('title')

            data['items'].append({'name': name, 'price': price})

        json.dump(data, file, indent=4, ensure_ascii=False)

def get_pagination():
    data = {}
    data['items'] = []

    url = 'https://www.labirint.ru/genres/2304/'

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    pagination = int(soup.find('div', class_='pagination-number__right').find \
                                ('a', class_='pagination-number__text').text)

    for page in range(1, pagination + 1):
        url = f'https://www.labirint.ru/genres/2304/?page={page}'
        get_data(url, data)
        print(f'[+] Complete {page}/{pagination} pages')

def main():
    get_pagination()
    finish_time = time() - start_time
    print(f'Total time: {round(finish_time, 2)} sec.')
'''

if __name__ == '__main__':
    main()