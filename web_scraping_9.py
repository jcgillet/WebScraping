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
    import re
    response = requests.get('http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.htm')
    doc = html.fromstring(response.text)
    l = [x.getchildren()[0].getchildren()[0].text for x in doc.cssselect('tr') if x.getchildren()[1].text == 'Rejected']

    res = 0

    for i in l:
        m = re.search('\((\d+)-(\d+)\)',i)
        if int(m.group(2))-int(m.group(1)) < 5:
            res+=1

    print res


if __name__ == '__main__':
    main()


    
