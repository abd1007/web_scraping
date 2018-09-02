'''
Requests allows you to send organic, grass-fed HTTP/1.1 requests,
without the need for manual labor.
'''
import requests

'''
Beautiful Soup is a Python package for parsing HTML and XML documents.
'''
from bs4 import BeautifulSoup
import pandas as pd

'''
requests.get(url).text will ping a website and return you HTML of the website.
'''
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text


soup = BeautifulSoup(website_url, 'lxml')

'''
Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document.
'''
soup.prettify()

'''
Name of the countries which we intend to extract is under class Wikitable Sortable.
'''
my_table = soup.find('table', {'class' : 'wikitable sortable'})

'''
Extract all the links within <a>
'''
links = my_table.findAll('a')

countries = []
for link in links:
    countries.append(link.get('title'))

'''
prints list of countries
'''
print(countries)

'''
Storing in pandas dataframe
'''
df = pd.DataFrame()
df['Countries'] = countries
print(df)