import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Башня'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    header = soup.find('h1').text
    definition =soup.find('p').text
    print(f'Термин: {header}')
    print(f'Определение: {definition}')
else:
    print(f'Не удалось подключться к странице. Статус код: {response.status_code}')