import json

__author__ = 'upaang'
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
data_map = []
obj_data = {}
for row in BeautifulSoup(s[0])("tr"):
    # print row
    if count==0:
        for cell in row("td"):
            # print cell.text
            if cell.text=='Recharge':
                continue
            obj_data[str(cell.text)] = ""
        count += 1
        # print obj_data
    elif count < 5000:
        val = 0
        obj_data={}
        obj_data_val={}
        for cell in row("td"):
            # print cell.text
            if val==0:
                obj_data["Denomination(Range)"] = str(cell.text)
            if val == 1:
                obj_data["TalkTime Range Value (Rs)"] = str(cell.text)
            if val == 2:
                obj_data["Processing Fee (Rs)"] = str(cell.text)
            if val == 3:
                obj_data["Service tax (Rs)"] = str(cell.text)
            if val == 4:
                obj_data["Validity (days)"] = str(cell.text)
            if val == 5:
                obj_data["Category"] = str(cell.text)
            val += 1
            # val=0
            # print cell.text
            # print obj_data
        data_map.append(obj_data)
        count += 1

        # print obj_data

# print data_map
print json.dumps(data_map)