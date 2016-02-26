#-------------------------------------------------------------------------------
# Name:        webScrape3
# Purpose:     number of people who visited a U.S. government website using
#              Internet Explorer 6.0 in the last 90 days
#
# Author:      jcg
#
# Created:     26/02/2016
# Copyright:   (c) jcg 2016
#-------------------------------------------------------------------------------

def main():
    from lxml import html
    import requests
    response = requests.get('http://analytics.usa.gov/data/live/ie.json')
    print(response.json()['totals']['ie_version']['6.0'])

if __name__ == '__main__':
    main()
