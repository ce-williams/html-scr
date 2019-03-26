import requests
import re

# get the data
data = requests.get('file:///Users/curtiswilliams6/Documents/1dev/Python/html-scr/scr.html')

# extract the phone numbers, emails, whatever
phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

print(phones, emails)