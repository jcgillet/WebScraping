#-------------------------------------------------------------------------------
# Name:        webScrape2
# Purpose:     The name of the most recently added dataset on data.gov
#
# Author:      jcg
#
# Created:     26/02/2016
# Copyright:   (c) jcg 2016
#-------------------------------------------------------------------------------

def main():
    from lxml import html
    import requests
    response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc')
    doc = html.fromstring(response.text)
    print(doc.cssselect('h3 a')[0].text)

if __name__ == '__main__':
    main()
