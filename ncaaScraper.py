from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import random
import json
import numpy as np
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from gSheet import sendToGoogleSheets


from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from bs import getLinks

def scraperFunc():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #https://stackoverflow.com/questions/65443542/why-doesnt-instagram-work-with-selenium-headless-chrome
    #This section is needed so that instagram does not block you from accessing the page
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-data-dir=/tmp/tarun")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430 Safari/537.36")

    
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options) #For first time 
    driver.implicitly_wait(30)
    Schools = []
    playerStats = []
    tempplayer = []
    links = getLinks()
    for link in links:
        print("HERE")
        link = "https://www.cbssports.com"+link
        #driver.get(link)
        time.sleep(2)
        link = link.replace("/roster/", "")
        print(link)
        driver.get(link)
        time.sleep(2)
        try:
            teamName = driver.find_element_by_xpath('//*[@id="PageTitle-header"]').text        
        except:
            time.sleep(10)
            teamName = driver.find_element_by_xpath('//*[@id="PageTitle-header"]').text
        print(teamName)
        time.sleep(2)
        try:
            division = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[3]/div[1]/div/div/div/table/tbody/tr[2]/td[1]').text
        except:
            time.sleep(10)
            division = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[3]/div[1]/div/div/div/table/tbody/tr[2]/td[1]').text

        print(division)
        time.sleep(2)
        link = (link+"/roster/")
        driver.get(link)
        time.sleep(3)
        for i in range(1, 100):
            print(i)
            dict2 = {"i":i}
            temp = []
            name1 = ('//*[@id="TableBase"]/div/div/table/tbody/tr[{i}]/td[2]/span[1]/span/a').format_map(dict2)
            number1 = ('//*[@id="TableBase"]/div/div/table/tbody/tr[{i}]/td[1]').format_map(dict2)
            homeSt1 = ('//*[@id="TableBase"]/div/div/table/tbody/tr[{i}]/td[3]').format_map(dict2)
            position1 = ('//*[@id="TableBase"]/div/div/table/tbody/tr[{i}]/td[7]').format_map(dict2)
            try:
                name = driver.find_element_by_xpath(name1).get_attribute("href")
                name = name.replace('https://www.cbssports.com/collegebasketball/players/playerpage/', '')
                number = driver.find_element_by_xpath(number1).text
                homeSt = driver.find_element_by_xpath(homeSt1).text
                position = driver.find_element_by_xpath(position1).text
                print("NAME:"+str(name))
                print(number)
                print(homeSt)
                print(position)


                

                temp.append(name)
                temp.append(number)
                temp.append(position)
                temp.append(division)
                temp.append(teamName)
                temp.append(homeSt)
                playerStats.append(temp)
                tempplayer.append(temp)

                #print(("There are {i} players added").format_map(dict2))
            except Exception as e:
                print(e)
                print("No more athletes on this team")
                df = pd.DataFrame((tempplayer), columns=['Name', 'Number', 'Positin', 'Division', 'teamName', 'HomeSt'])
                print("ADDING TO GOOGLE SHEET!")
                sendToGoogleSheets(df)
                tempplayer = []
                driver.get('https://www.cbssports.com/collegebasketball/players')
                break



            
    df = pd.DataFrame((playerStats), columns=['Name', 'Number', 'Positin', 'Division', 'teamName', 'HomeSt'])
    print(df)
    return df
    #df.to_csv(r'Players.csv', index = False)





        
    print('success')