# Adapted from https://github.com/compjour/search-script-scrape/blob/master/scripts/1.py

from lxml import html
import requests
response = requests.get('http://www.data.gov/')
doc = html.fromstring(response.text)
print([x.text for x in doc.cssselect('h4 label small a')])
