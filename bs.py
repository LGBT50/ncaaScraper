import bs4
import urllib.request
from bs4 import BeautifulSoup
import requests

def getLinks():
   r = requests.get('https://www.cbssports.com/college-basketball/teams/')

   soup = BeautifulSoup(r.text, "html.parser")

   anchors = soup.find_all('a', {"href":True})
   #print(anchors)
   links = []
   for anchor in anchors:
      #print(type(anchor['href']))
      if "roster" in str(anchor['href']):
         links.append(anchor["href"])
   return links
getLinks()