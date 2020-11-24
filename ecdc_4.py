# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:40:21 2020

@author: jsyme
"""
#import os
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
import urllib.request
from urllib.error import HTTPError

### this reads a given worksheet from the source excel
def create_df(path,x):
    df = pd.read_excel(filenm, sheet_name=path, header = [x])
    return df

# not used
'''
# I've left this in cos we will need final output to xls when we also
# do deaths as a csv is only a single worksheet
def save_xls(usedf, usenm):
    with ExcelWriter(xls_path) as writer:
        usedf.to_excel(writer,usenm)
        writer.save()
'''

###Import country populations 
filenm = 'C:\\Users\\jsyme\\Documents\\Q_Macro\\Weekly_dashboard\\countrypops.xlsx'
countrypops = create_df('pops',0)
#citypops=citypops.T

'''
###Create unique name to save the file as
now=datetime.now()
date_time = now.strftime("%d%B%Y_%H%M%S")
userfilename='pfloader_output_'+date_time+'.xls'
'''

### create URL link to xls

print(filenm)

### create df
now=datetime.now()
try:
    filenm = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-'+now.strftime("%Y")+'-'+now.strftime("%m")+'-'+now.strftime("%d")+'.xlsx'
    coviddf = create_df('COVID-19-geographic-disbtributi', 0)
except urllib.error.HTTPError as err:
    try:
        filenm = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-'+now.strftime("%Y")+'-'+now.strftime("%m")+'-'+str(now.day-1)+'.xlsx'
        coviddf = create_df('COVID-19-geographic-disbtributi', 0)
    except urllib.error.HTTPError as err:
        print('Failed - File not found')
        print(err.code)

### set index and make index datetime
coviddf.set_index('dateRep', inplace = True)
coviddf.index = pd.to_datetime(coviddf.index)

countrylist = ['BR', 'CL', 'MX','AE','PL','RU', 'SA', 'TR', 'ZA', 'ID', 'MY',
               'PH', 'TH', 'IN', 'TW', 'KR', 'CN']

datas = ['cases','deaths']
for datat in datas:
    
    for i in countrylist:
        coviddf1 = coviddf[coviddf['geoId'] == i]
        ### take weekly data
        ### by taking (average * 7) I get a weekly rate even if most recent
        ### week hasn't finished yet
        outdf1 = coviddf1[datat].resample('W').mean()
        outdf1 = outdf1 * 7
        ### rename series
        outdf1 = outdf1.rename(i)
        ### this creates an output df with the first country in the list
        ### in order to have something to merge with
        if i == countrylist[0]:
            outdf = outdf1
        else:
            ### merge output dataframes into the final
            outdf = pd.merge(outdf,outdf1,how='outer', on='dateRep')
    
    outdf2 = outdf.copy()
    for j in outdf.columns:
        pop = countrypops[j][0]
        outdf2[j] = outdf[j].apply(lambda x: x/pop)
    
    #create datetime string for output filename
    now=datetime.now()
    date_time = now.strftime("%d%B%Y_%H%M%S")
    #Create unique name to save the file as
    userfilename='Covid_weekly_'+datat+date_time+'.csv'
    userfilename2='Covid_weekly_2_'+datat+date_time+'.csv'
    userfilename3='Covid_weekly_'+datat+'.csv'
    
    
    #push df to csv
    outdf.to_csv(userfilename)
    outdf2.to_csv(userfilename2)
    outdf2.to_csv(userfilename3)
    


