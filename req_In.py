from bs4 import BeautifulSoup

import requests


html = requests.get('https://www.linkedin.com/in/marcosvile').content

soup = BeautifulSoup(html, 'html.parser')

print (soup.prettify())