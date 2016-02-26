#-------------------------------------------------------------------------------
# Name:        webScrape2
# Purpose:     Number of days until Texas’s next scheduled execution
#
# Author:      jcg
#
# Created:     26/02/2016
# Copyright:   (c) jcg 2016
#-------------------------------------------------------------------------------

def main():
    from lxml import html
    import requests
    import time
    response = requests.get('http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html')
    doc = html.fromstring(response.text)
    s = doc.cssselect('td')[0].text
    print((datetime.strptime(s,'%m/%d/%Y')-datetime.today()).days)

if __name__ == '__main__':
    main()
