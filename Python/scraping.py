import requests
from bs4 import BeautifulSoup

print('Start scraping read application')

pagina = requests.get('https://coinmarketcap.com')
#print(pagina.content)

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')
table = heeldehtml.find('table')
print(table.prettify())