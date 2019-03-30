import requests 
from bs4 import BeautifulSoup

# get the data

data = requests.get('https://coinmarketcap.com')


# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# get data simply by looking for each tr

for tr in soup.find_all('td'):
    values = [td.val for td in tr.find_all('td')]
    print(values)