
from googlesearch import search

from rGoogleSheet import rGSheet

import pandas as pd
import time

from linkGSheet import lSheet
def instaLink():
    #googleTrendsUrl = 'https://google.com'
    #response = requests.get(googleTrendsUrl)
    #if response.status_code == 200:
    #    g_cookies = response.cookies.get_dict()
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
    #        AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
    #url = 'https://www.google.com?q=' + query
    names = rGSheet()
    links = []
    counter = 0
    linkList = []
    for x in names:
        counter +=1
        query = str(x)
        x = 0
        print(len(links))

        for j in search(query):
            if "instagram" in j:
                x+=1
                links.append(j)
                link = j
                break
        if x <1:
            query = query + " basketball instagram"
        time.sleep(1)
        for j in search(query):
            if x == 1:
                break
            if "instagram" in j:
                x+=1
                links.append(j)
                link = j
                break
        time.sleep(1)

        temp = []
        temp.append(link)
        linkList.append(temp)
        if len(linkList) % 10 == 0:
            df = pd.DataFrame((linkList), columns=["Links"])
            print(df)
            lSheet(df)

    

        

    #df = pd.DataFrame((linkList), columns=["Links"])
    #lSheet(df)




    