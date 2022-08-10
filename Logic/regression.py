
import csv
from re import S
from tabnanny import check
from typing_extensions import Self
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

def getCorr():

    df1 = pd.read_csv('Bond yield data/EU/eUData.csv', usecols=['time', 'CCIdata'])
    df2 = pd.read_csv('Bond yield data/EU/eUData.csv', usecols=['time', 'yieldData'])

    for i in range(1, 12):
        
        df1['CCIdata'] = df1['CCIdata'].shift((i))

        fig, ax1 = plt.subplots() 
    
        ax1.set_xlabel('Time') 
        ax1.set_ylabel('EU05Y-EU03MY', color = 'red') 
        ax1.plot(df2['time'], df2['yieldData'], color = 'red') 
        ax1.tick_params(axis ='y', labelcolor = 'red') 
        
        ax2 = ax1.twinx() 
        
        ax2.set_ylabel('CCIdata', color = 'blue') 
        ax2.plot(df1['time'], df1['CCIdata'], color = 'blue') 
        ax2.tick_params(axis ='y', labelcolor = 'blue') 
        
        spearmanCorrelation = df1['CCIdata'].corr(df2['yieldData'], method='spearman')
        pearsonCorrelation = df1['CCIdata'].corr(df2['yieldData'], method='pearson')
        kendallCorrelation = df1['CCIdata'].corr(df2['yieldData'], method='kendall')

        print(f'shift by {i}')
        print(f'Spearman: {spearmanCorrelation}, Pearson: {pearsonCorrelation}, Kendal: {kendallCorrelation}')

        plt.show()

def checkStationarityADF():

    df1 = pd.read_csv('Bond yield data/EU/eUData.csv', usecols=['time', 'CCIdata'])
    df1 = df1.dropna()
    df2 = pd.read_csv('Bond yield data/EU/eUData.csv', usecols=['time', 'yieldData'])
    df2 = df2.dropna()

    x = adfuller(df1['CCIdata'])
    y = adfuller(df2['yieldData'])

    print('ADF Statistic: %f' % x[0])
    print('p-value: %f' % x[1])
    print('Critical Values:')
    for key, value in x[4].items():
        print('\t%s: %.3f' % (key, value))

    print('ADF Statistic: %f' % y[0])
    print('p-value: %f' % y[1])
    print('Critical Values:')
    for key, value in y[4].items():
	    print('\t%s: %.3f' % (key, value))

def checkStationarityKPSS():

    df1 = pd.read_csv('Bond yield data/EU/eUData.csv', usecols=['time', 'EUCCI'])
    df2 = pd.read_csv('Bond yield data/EU/eUData.csv', usecols=['time', 'yield%'])

    x = kpss(df1['EUCCI'], regression="ct")
    y = kpss(df2['yield%'], regression="ct")

    print('Test Statistic: %f' %x[0])
    print('p-value: %f' %x[1])
    print('Critical values:')
    for key, value in x[3].items():
        print('\t%s: %.3f' %(key, value))
    
    print('Test Statistic: %f' %y[0])
    print('p-value: %f' %y[1])
    print('Critical values:')
    for key, value in y[3].items():
        print('\t%s: %.3f' %(key, value))

def differenceData():

    df1 = pd.read_csv('Bond yield data/EU/eUData.csv')
    df1['CCIdata'] = df1['EUCCI'].diff()
    df1['yieldData'] = df1['yield%'].diff()
    df1.to_csv('Bond yield data/EU/eUData.csv')

getCorr()