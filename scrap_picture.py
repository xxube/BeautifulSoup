# -*- coding: utf-8 -*-
"""scrap picture.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NVJDLJcC4_AN3X1aONu4pPuwD6E6ElyD
"""

import requests
from bs4 import BeautifulSoup as bs

url = 'https://keithgalli.github.io/web-scraping/'
r = requests.get(url+'webpage.html')
webpage = bs(r.content)

images = webpage.select('div.row div.column img')
image_url = images[0]['src']
full_image_url = url + image_url

image_data = requests.get(full_image_url).content
##with open('picture1.jpg', 'wb') as handler:  ## with open
##handler.write(image_data)