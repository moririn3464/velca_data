from typing import Text
import requests
import bs4


spnav_url = 'https://sportsnavi.ht.kyodo-d.jp/basketball/stats/b3/score/7027/box/h'


def getsoup(url):
  res = requests.get(url)
  try:
    res.raise_for_status()
  except requests.exceptions.HTTPError
  html = """<html><head><title>Error</title></head></html>"""
  soup = bs4.BeautifulSoup(html,'lxml')
  else:
    soup = bs4.BeautifulSoup(res.text, 'lxml')
  finally:
    return soup

  
def spnav_scraping():
  soup = getsoup(spnav_url)
  elem = soup.select('td')

  list = []
  for elem in elems:
    text = elem.getText()
    return list

    