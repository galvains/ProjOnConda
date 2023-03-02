import requests
from random import choice
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}

phone_number = '+79493091683'

response = requests.get('https://fox-pizza.ru/auth/', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
sessid = soup.find('input').get('value').strip()


data = {
    'PHONE': phone_number,
    'sessid': sessid
}
print(data)

requests.post("https://api.fix-price.com/buyer/v2/registration/phone/request", data={"phone": phone_number})
print(response.status_code)

