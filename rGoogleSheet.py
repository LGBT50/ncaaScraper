from oauth2client.service_account import ServiceAccountCredentials
import gspread
from gspread_dataframe import set_with_dataframe
import gspread_dataframe as gd
import pandas as pd



def rGSheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets']

    #Generate a json file by using service account auth in google developer console
    '''
    Link: https://console.developers.google.com/
    1) Enable API Access for a Project if you haven’t done it yet.
    2) Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
    3) Fill out the form
    4) Click “Create” and “Done”.
    5) Press “Manage service accounts” above Service Accounts.
    6) Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
    7) Select JSON key type and press “Create”.
    '''
    creds = ServiceAccountCredentials.from_json_keyfile_name('mod.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1_xpIRMPw3U-eDGRp84HOH153-kumeA-T0NVJfaBQ-_s/edit#gid=0").sheet1

    data = sheet.get_all_records()
    #print(len(data))
    df1 = pd.DataFrame(data, columns=['Name', 'Number', 'Positin', 'Division', 'teamName', 'HomeSt'])
    #print(df1)
    #for x in df1["name"]:
        #print(x)

    print(type(df1["Name"]))
    list1 = df1['Name'].tolist()
    #print(list1)
    counter = 0
    new = []
    for x in list1:
      
        for c in x:
            if c != "/":
                x = x.replace(c, "")
            if  c == "/":
                x = x.replace(c, "")
                print(x)
                x = x.replace("-", " ") 
                new.append(x)
                break


            
    return new
                

    