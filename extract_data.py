__author__ = 'minjar86'
import json
import urllib2
from BeautifulSoup import BeautifulSoup

url='http://www.airtel.in/mobile/prepaid/recharge-online?CIRCLE=2&CIRCLENAME=Delhi%20NCR&tab=1#tabs-1'
request=urllib2.Request(url=url)
handle=urllib2.urlopen(request)

content= handle.read()
# print content
split_page=content.split("<div class=\"collapse shown\">",1)
s=split_page[1].split("</div>",1)
# print s[0]
count=0
data_map={}
for row in BeautifulSoup(s[0])("tr"):
    print row
    if count==0:
        for cell in row("td"):
            # print cell.text
            count+=1
            data_map[str(cell.text)]=""
        print data_map
    else:
        for cell in row("td"):
            val=0
            if val==0:
                data_map["Denomination(Range)"]=cell.text
            print cell.text
