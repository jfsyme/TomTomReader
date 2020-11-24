# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:41:25 2020

@author: jsyme
"""

from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
import urllib.request
from urllib.error import HTTPError


## Use raw github url 
url= "https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/summary_reports/summary_report_countries.csv"
data=pd.read_csv(url)

countrylist = ['Argentina', 'Brazil', 'Chile','Colombia','Peru','Mexico','United Arab Emirates','Saudi Arabia','Qatar','Turkey',
               'Greece','Poland','Hungary','Czechia','Russia','South Africa','China','India','Pakistan','Taiwan',
               'South Korea','Indonesia','Malaysia','Thailand','Philippines']
countryoutlist=[]

#select only Argentina
wkdf = data[data['country'] == 'Argentina']
#select only workplaces
wkdf1 = wkdf[['date','workplaces']]
### set index and make index datetime
wkdf1.set_index('date', inplace = True)
wkdf1.index = pd.to_datetime(wkdf1.index)
### take weekly data average
wkdf2 = wkdf1['workplaces'].resample('W').mean()

datas = ['workplaces','driving','transit']
for datat in datas:
    
    for i in countrylist:
        wkdf = data[data['country'] == i]
        wkdf1 = wkdf[['date',datat]]
        ### set index and make index datetime
        wkdf1.set_index('date', inplace = True)
        wkdf1.index = pd.to_datetime(wkdf1.index)
        ### take weekly data average
        wkdf2 = wkdf1[datat].resample('W').mean()
        ### rename series
        wkdf2 = wkdf2.rename(i)
        ### this creates an output df with the first country in the list
        ### in order to have something to merge with
        if i == countrylist[0]:
            outdf = wkdf2
        else:
            ### merge output dataframes into the final
            outdf = pd.merge(outdf,wkdf2,how='outer', on='date')
    
    #create datetime string for output filename
    now=datetime.now()
    date_time = now.strftime("%d%B%Y_%H%M%S")
    #Create unique name to save the file as
    userfilename='Mobility_weekly_'+datat+date_time+'.csv'
    
    #push df to csv
    outdf.to_csv(userfilename)
