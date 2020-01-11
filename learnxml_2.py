import xml.etree.ElementTree as ET
import urllib.parse, urllib.error, urllib.request

count = 0
url = "http://py4e-data.dr-chuck.net/comments_300115.xml"
# with open("comments_300115.xml","r") as xmlfile:
#     xmltree = ET.fromstring(xmlfile.read())
#     lstxml = xmltree.findall('comments/comment')
#     for num in lstxml:
#         # print('Number',num.find('count').text)
#         count += int(num.find('count').text)
dataxml = urllib.request.urlopen(url)
xmlfile = dataxml.read()
xmltree = ET.fromstring(xmlfile)

lstxml = xmltree.findall('comments/comment')

for num in lstxml:
    count += int(num.find('count').text)

print(count)