

import pandas as pd
import numpy as np
import datetime as dt

df = pd.read_csv('Bond yield data/US/TVC_US05Y, 1D.csv')
df['time'] = pd.to_datetime(df['time'], errors='coerce')

def getFirstDayOfMonth():

    for i in range(1987, 2023):
        yearMask = df['time'].dt.year == int(i)
        yearInclude = df[yearMask].copy(deep=True)
        yearInclude['time'] = pd.to_datetime(yearInclude['time'])

        for j in range(1, 13):
            monthMask = yearInclude['time'].dt.month == int(j)
            monthInclude = yearInclude[monthMask]
            temp = monthInclude.head(1).copy(deep=True)
            temp.to_csv('Bond yield data/UK/TVC_GB05Y, 1M.csv', mode='a', index=False, header=False)

def removeTimeDayOnDate():

    # df['time'] = df['time'].dt.date
    df['time'] = df['time'].dt.strftime('%Y-%m')
    df.to_csv('Bond yield data/UK/TVC_GB05Y, 1M.csv', mode='a', index=False, header=False)

def aggregateData():
    
    df1 = pd.read_csv('Bond yield data/UK/TVC_GB05Y, 1M Normalised.csv')
    df2 = pd.read_csv('Bond yield data/UK/GBRCCI, 1M Normalised.csv')

    data = [df1['time'], df1['GB05YClose'], df1['GB03MYClose'], df2['Value']]

    headers = ['time', 'GB05Y', 'GB03MY','GBCCI']

    df3 = pd.concat(data, axis=1, keys=headers)

    df3['yield%'] = df3['GB05Y'] - df3['GB03MY']

    print(df3.head())

    df3.to_csv('Bond yield data/UK/gbData.csv')

getFirstDayOfMonth()
# # removeTimeDayOnDate()
# aggregateData()

