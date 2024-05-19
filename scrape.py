# -*- coding: utf-8 -*-
"""scrape.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yLU5Et-nwRT1S3GgQ09sKwtbe-cP2LAS

## Loading necessary libraries
"""

import requests ## pip instal requests
from bs4 import BeautifulSoup as bs ## pip instal beautifulsoup4

"""##Load our first page"""

# Load the webpage content
r = requests.get('https://keithgalli.github.io/web-scraping/example.html')

#convert to a beautifulsoup object
soup = bs(r.content)

print(soup.prettify())

"""##find and find all"""

import re
header = soup.find("h1")

headers = soup.find_all('code')

paragraph = soup.find(attrs = {'id':'suggestions'})
paragraphs = soup.find_all(string = re.compile('(L|l)ogo'))
paragraphs

content = soup.select('div h1')
content2 = soup.select('h2 ~ p')
content2

Bold_text = soup.select('p#paragraph-id b')
Bold_text

paragraphs = soup.select('body > p')
print(paragraphs)

for paragraph in paragraphs:
  print(paragraph.select('i'))

##select elements by property
soup.select('[id="paragraph-id"]')

"""##get different properties of HTML"""

# Load the webpage content
r = requests.get('https://keithgalli.github.io/web-scraping/webpage.html')

#convert to a beautifulsoup object
webpage = bs(r.content)

print(webpage.prettify())

links = webpage.select('ul.socials a')
actual_links = [link['href'] for link in links]
actual_links

web_links = webpage.find('ul', attrs={'class':'socials'})
 links = web_links.find_all('a')
 actual_links = [link['href'] for link in links]
 actual_links

links = webpage.select('li.social a')
actual_links = [link['href'] for link in links]
actual_links

import pandas as pd

table_data = webpage.select('table.hockey-stats')[0]


columns = table_data.find('thead').find_all('th')
columns_names = [c.string for c in columns]

table_rows = table_data.find('tbody').find_all('tr')

l = []
for tr in table_rows:
  td = tr.find_all('td')
  row = [str(tr.get_text()).strip() for tr in td]
  l.append(row)

df = pd.DataFrame(l, columns = columns_names)
df.loc[df['Team'] != 'Did not play'].sum()

"""##Grab all fun facts that use word 'is'

"""

facts = webpage.select("ul.fun-facts li")
facts_with_is = [fact.find(string=re.compile('is')) for fact in facts]
facts_with_is = [fact for fact in facts_with_is if fact]
facts_with_is

"""##Solve the Mystery Message Challenge!"""

Mystery_Message = webpage.select('div.block a')
files_url = [f['href'] for f in Mystery_Message]

url = 'https://keithgalli.github.io/web-scraping/'

for f in files_url:
  files_full_url = url + f
  files = requests.get(files_full_url)
  bs_files = bs(files.content)

  secret_word = bs_files.find('p', attrs = {'id': 'secret-word'})
  secret_word = secret_word.string
  print(secret_word)