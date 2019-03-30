import requests
from bs4 import BeautifulSoup

r = requests.get('https://coinmarketcap.com/all/views/all')
soup = BeautifulSoup(r.text, 'lxml')

# data = []
# bitcoin = soup.find('table', id='id_bitcoin')
# for row in bitcoin.find('td'):
#     try:
#         symbol = row.find('td', 'text-left col-symbol').text
#         price = row.find('a', class_='price').text
#         time_1h = row.find('td', {'data-timespan': '1h'}).text
#     except AttributeError:
#         continue
# data.append((symbol, price, time_1h))

# for item in data:
#     print(data)


title = soup.find_all('tr', limit=10)
print(title)


# ////////////////////////////////////
# ///////////ALL CURRENCIES///////////
# ////////////////////////////////////
# data = []
# table = soup.find('table', id='currencies-all')
# 
# for row in table.find_all('tr'):
#     try:
#         symbol = row.find('td', 'text-left col-symbol').text
#         price = row.find('a', class_='price').text
#         time_1h = row.find('td', {'data-timespan': '1h'}).text
#     except AttributeError:
#         continue
#     data.append((symbol, price, time_1h))
# for item in data:
#     print(data)