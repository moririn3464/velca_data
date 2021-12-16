import urllib.request
from bs4 import BeautifulSoup


spnav_url = urllib.request.urlopen('https://sportsnavi.ht.kyodo-d.jp/basketball/stats/b3/score/7027/box/h')
html = spnav_url.read().decode('utf-8', 'ignore')
parser = "html.parser"
soup = BeautifulSoup(html, parser)

title = soup.find("title").text
print(title)
