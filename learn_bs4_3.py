from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def lastLink(getlink):
    seq = 0
    html = urlopen(getlink).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
        seq += 1
        if seq == 18:
            getlink = str(tag.get('href', None))
            return getlink

url = "http://py4e-data.dr-chuck.net/known_by_Conlyn.html"
# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

# Retrieve all of the anchor tags
for item in range(1,8):
    url = lastLink(url)
    print(url)