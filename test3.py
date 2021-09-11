import requests
import bs4
import urllib.request
from bs4 import BeautifulSoup
from googlesearch import search
import random

from rGoogleSheet import rGSheet

import pandas as pd
import time

from linkGSheet import lSheet

def importAgents():
    lines = []
    with open("user-agent-list.txt") as file:
        while (line := file.readline().rstrip()):
            lines.append(line)
    return lines

def getRandomAgent():
    agents = importAgents()
    randomAgent = random.choice(agents)
    return randomAgent

def creds():
    headers = {'User-Agent': getRandomAgent()}
    googleTrendsUrl = 'https://google.com'
    response = requests.get(googleTrendsUrl, headers)
    if response.status_code == 200:
        g_cookies = response.cookies.get_dict()
    headers = {'User-Agent': getRandomAgent()}
    credentials = {"head": headers, "cookies":g_cookies}
    return credentials
    
def getLink():
    links = []
    names = rGSheet()
    counter = 0
    for name in names:

        query = name
        query = query+" basketball instagram"
        query = query.replace(" ", "+")
        url = 'https://www.google.com/search?q=' + query
        if counter == 0:
            credentials = creds()
        res = requests.get(url, headers = credentials["head"], cookies = credentials["cookies"])
        if res == 200 or counter%50==0:
            credentials = creds()
            res = requests.get(url, headers = credentials["head"], cookies = credentials["cookies"])
        soup = BeautifulSoup(res.text, "html.parser")
    #output = []

        anchors = soup.find_all('a', {"href":True})

        for anchor in anchors:
            if "instagram.com" in anchor["href"]:
                print(anchor["href"])
                links.append(anchor["href"])
                break
        if len(links) > 10:
            addToGsheet(links)
            links = []
        print(counter)
        counter += 1



def addToGsheet(linkList):
    df = pd.DataFrame((linkList), columns=["Links"])
    print(df)
    lSheet(df)