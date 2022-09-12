#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import plotly
import plotly.express as px
import arabic_reshaper
from bidi.algorithm import get_display


# In[15]:


import pandas as pd
from google.oauth2.credentials import Credentials

from googleapiclient.discovery import build


from google.oauth2 import service_account
def get_sheet(id):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'keys.json'

    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,scopes=SCOPES)

    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = id







    service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range='A1:M100').execute()
    values = result.get('values', [])
    
    df = pd.DataFrame(values[1:], columns=values[0])
    return df

#get_sheet('1wMi1a_Igifrz4MtM4nsbXA-SAl7Mo9uO85nVpW-rL_Q')


# In[3]:


def add_date(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['month']=df['Timestamp'].dt.month
    df['day']=df['Timestamp'].dt.day
    df['year']=df['Timestamp'].dt.year
    return df


# In[4]:


def rename(df):
    try:
        df['name'] = df['لطفا نام خود را وارد نمائید'] 
        df['peronal'] = df['لطفا کد پرسنلی خود را ثبت نمائید.'] 
        df['team'] = df['لطفا واحدی که در آن مشغول به فعالیت می باشید را انتخاب نمائید.']
        df['description'] = df['لطفا پیشنهاد خود را شرح دهید:']
        df['field'] = df["پیشنهاد شما در چه حوزه ای می باشد؟"]
        df['documentation'] = df['در صورت نیاز به بارگزاری مستندات برای شفافیت موضوع خود، میتوانید از این قسمت استفاده نمائید.']
    except : pass
    
    return df


# In[5]:


def preprocessing(df):
    df['peronal'] = df['peronal'].astype(int)
    df['name'] = df['name'].astype(str)
    df['team'] = df['team'].astype(str)
    
    return df


def main():
    df = get_sheet('1wMi1a_Igifrz4MtM4nsbXA-SAl7Mo9uO85nVpW-rL_Q')
    df = add_date(df)
    df = rename(df)
    df = preprocessing(df)
    df.head()
    ax = sns.displot(df.team)
    ax.tick_params(axis='x', rotation=90)
    plt.show()
    
    t = sns.displot(df.field)
    t.tick_params(axis='x', rotation=90)
    
    
    

    
    
    
    
if __name__ == '__main__':
    main()



