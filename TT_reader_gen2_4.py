
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 23:34:35 2020

@author: James
"""
### Overview of code structure
### 0 Imports and variable set up
### 1 Call city data from TT
### 2 Import city populations from Excel
### 3 Arrange and clean both
### 4 Produce population-weighted congestion average at a country level
### 5 Output to Excel

### 0 Imports and variable set up

from datetime import datetime
import pandas as pd
import json
import requests

#define list of cities as per URLs
citylist = ['ARE_abu-dhabi',
'ARE_dubai',
'ARG_buenos-aires',
'BRA_belo-horizonte',
'BRA_brasilia',
'BRA_curitiba',
'BRA_fortaleza',
'BRA_porto-alegre',
'BRA_recife',
'BRA_rio-de-janeiro',
'BRA_salvador',
'BRA_sao-paulo',
'CHL_santiago',
'CHN_beijing',
'CHN_changchun',
'CHN_changsha',
'CHN_chengdu',
'CHN_chongqing',
'CHN_dongguan',
'CHN_fuzhou',
'CHN_guangzhou',
'CHN_hangzhou',
'HKG_hong-kong',
'CHN_nanjing',
'CHN_ningbo',
'CHN_quanzhou',
'CHN_shanghai',
'CHN_shenyang',
'CHN_shenzhen',
'CHN_shijiazhuang',
'CHN_suzhou',
'CHN_tianjin',
'CHN_wuhan',
'CHN_wuxi',
'CHN_xiamen',
'CHN_zhuhai',
'COL_bogota',
'CZE_brno',
'CZE_ostrava',
'CZE_prague',
'EGY_cairo',
'GRC_athens',
'GRC_thessaloniki',
'HUN_budapest',
'IDN_jakarta',
'IND_bangalore',
'IND_mumbai',
'IND_new-delhi',
'IND_pune',
'MEX_mexico-city',
'MYS_kuala-lumpur',
'PER_lima',
'PHL_manila',
'POL_bialystok',
'POL_bydgoszcz',
'POL_gdansk-gdynia-sopot',
'POL_katowice-urban-area',
'POL_krakow',
'POL_lodz',
'POL_lublin',
'POL_poznan',
'POL_szczecin',
'POL_warsaw',
'POL_wroclaw',
'RUS_chelyabinsk',
'RUS_kazan',
'RUS_moscow',
'RUS_nizhny-novgorod',
'RUS_novosibirsk',
'RUS_omsk',
'RUS_saint-petersburg',
'RUS_samara',
'RUS_tomsk',
'RUS_yekaterinburg',
'SAU_jeddah',
'SAU_riyadh',
'THA_bangkok',
'TUR_adana',
'TUR_ankara',
'TUR_antalya',
'TUR_bursa',
'TUR_gaziantep',
'TUR_istanbul',
'TUR_izmir',
'TUR_kayseri',
'TUR_konya',
'TUR_mersin',
'TWN_kaohsiung',
'TWN_taichung',
'TWN_tainan',
'TWN_taipei',
'TWN_taoyuan',
'ZAF_bloemfontein',
'ZAF_cape-town',
'ZAF_durban',
'ZAF_east-london',
'ZAF_johannesburg',
'ZAF_pretoria']

'''
#temp citylist
citylist = ['ARE_abu-dhabi',
'ARE_dubai',
'ARG_buenos-aires',
'BRA_belo-horizonte',
'BRA_brasilia',
'BRA_curitiba']

'''
outlist=[]
outdict={}
faillist = []

### 1 Call city data from TT

for city in citylist:
    try:
        # retrieve json file
        url = "https://api.midway.tomtom.com/ranking/weeklyStats/"+city
        city_req = requests.get(url)
        city_json = city_req.json()

        #all this does is limit rows displayed if we do this
        pd.set_option("display.max_rows", False)
    
        congestion = []
        weekStart = []
    
        count = len(city_json)-1
    
        # append each item in the json file to the empty lists
        i=0
        while i<=count:
            congestion.append(city_json[i]["congestion"])
            weekStart.append(city_json[i]["weekStart"])
            i+=1
    
        # create dataframe with the traffic data 
        df = pd.DataFrame({"Congestion":congestion}, index=weekStart)
        #set index of dates
        df.index = pd.to_datetime(df.index)
        df.index.name = "weekStart"
        #rename column of congestion data to city name
        #spyder doesnt like this but it works
        df.columns = [city]
        
        outlist.append(df)
        outdict[city] = df

    except:
        faillist.append(city)

#print faillist to console

print('DID NOT COMPLETE:',faillist)

#outlist to a dataframe
result = pd.concat(outlist, axis=1, sort=False)
result = result.fillna(0)

### 2 Import city populations from Excel
 
def create_df(path,x):
    ### this reads a given worksheet from the source excel
    df = pd.read_excel('citypops.xlsx', sheet_name=path, header = [x])
    return df

citypops = create_df('pops',0)
#citypops = citypops[1:]


### 4 Produce population-weighted congestion average at a country level

ctrylist = []
for i in citylist:
    x = i[:3]
    if x in ctrylist:
        pass
    else:
        ctrylist.append(x)

#create a dict of country:[cities]
ctrydict = {k:[] for k in ctrylist}

for i in citylist:
    ctrydict[i[:3]].append(i)

ctryoutdict = {}
#create outdf with a city in it to give structure
outdf = result[result.columns[0]]
#loop through each country to
#i is country 
for i in ctrydict.keys():
    #list of cities in that country
    worklist = ctrydict[i]
    #empty df for pops in order
    orddpops = pd.DataFrame([])
    for j in worklist:
        orddpops = pd.concat([orddpops,citypops[j]], axis=1)
    #extend orddpops to length of city data
    orddpops_long = pd.concat([orddpops]*len(outlist[0]), ignore_index=True)
    orddpops_long['Date'] = result[j].index
    orddpops_long.set_index('Date', inplace = True)
 
    orddcong = pd.DataFrame([])
    for j in worklist:
        orddcong = pd.concat([orddcong,outdict[j]], axis=1)
    #multiply data by weights
    wtddata = (orddcong * orddpops_long)
    
    #sum weighted data and weights
    wtddata['sum'] = wtddata.sum(axis = 1)
    orddpops_long['sum'] = orddpops_long.sum(axis = 1)
    
    workdf = wtddata['sum'] / orddpops_long['sum']
    outdf = pd.concat([outdf,workdf], axis = 1)
    outdf = outdf.rename(columns={"sum": i})

#delete the city we started outdf with
outdf = outdf.drop(outdf.columns[0], 1)

### 5 Output to Excel

#create datetime string for output filename
now=datetime.now()
date_time = now.strftime("%d%B%Y_%H%M%S")
#Create unique name to save the file as
userfilename='TT_congestion_output_'+date_time+'.csv'

#result = pd.concat(outlist, axis=1, sort=False)

#push df to csv
outdf.to_csv(userfilename)

