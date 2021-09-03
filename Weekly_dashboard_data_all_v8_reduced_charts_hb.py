# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:33:44 2020

@author: jsyme
"""

###### IMPORTS #####

from datetime import datetime
import pandas as pd
import json
import requests
from functools import reduce
#from pandas import ExcelWriter
import urllib.request
from urllib.error import HTTPError
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.ticker as mtick


###EXTERNAL XLS DEPENDENCIES AT LINES 354 AND 452 AND 526

##### MOBILITY #####

def mobility_f():
    ## Use raw github url 
    url= "https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/summary_reports/summary_report_countries.csv"
    data=pd.read_csv(url)
    
    #loop through each data type
    for datat in datas:
        for i in countrylist:
            wkdf = data[data['country'] == i]
            wkdf1 = wkdf[['date',datat]]
            ### set index and make index datetime
            wkdf1.set_index('date', inplace = True)
            wkdf1.index = pd.to_datetime(wkdf1.index)
            ### take weekly data average
            wkdf2 = wkdf1[datat].rolling(7).mean()
            ### rename series
            wkdf2 = wkdf2.rename(country_ids[i])
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
        
        #add to dataoutdict
        dod[datat] = outdf
        dodnames.append(datat)
        
        #push df to csv
        outdf.to_csv(userfilename)

#setup for mobility
countrylist = ['Argentina', 'Brazil', 'Chile','Colombia','Peru','Mexico','United Arab Emirates','Saudi Arabia','Qatar','Turkey',
               'Greece','Poland','Hungary','Czechia','Russia','South Africa','China','India','Pakistan','Taiwan',
               'South Korea','Indonesia','Malaysia','Thailand','Philippines']
country_ids = {'Argentina':'AR', 'Brazil':'BR', 'Chile':'CL','Colombia':'CO','Peru':'PE',
               'Mexico':'MX','United Arab Emirates':'AE','Saudi Arabia':'SA','Qatar':'QA',
               'Turkey':'TR','Greece':'GR','Poland':'PL','Hungary':'HU','Czechia':'CZ',
               'Russia':'RU','South Africa':'ZA','China':'CN','India':'IN','Pakistan':'PK',
               'Taiwan':'TW','South Korea':'KR','Indonesia':'ID','Malaysia':'MY',
               'Thailand':'TH','Philippines':'PH'}

#reduced
countrylist = ['Brazil', 'Chile','Mexico','United Arab Emirates','Saudi Arabia','Turkey',
               'Poland','Russia','South Africa','China','India','Taiwan',
               'South Korea','Indonesia','Malaysia','Thailand','Philippines']

country_ids = { 'Brazil':'BR', 'Chile':'CL',
               'Mexico':'MX','United Arab Emirates':'AE','Saudi Arabia':'SA',
               'Turkey':'TR','Poland':'PL',
               'Russia':'RU','South Africa':'ZA','China':'CN','India':'IN',
               'Taiwan':'TW','South Korea':'KR','Indonesia':'ID','Malaysia':'MY',
               'Thailand':'TH','Philippines':'PH'}

country_names = {value:key for key, value in country_ids.items()}

dod = {}
dodnames = []
datas = ['workplaces','driving','transit']

#run mobility
mobility_f()

##### TOMTOM #####

#set up for TT
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

TTcountry_ids = {'ARE':'AE', 'ARG':'AR', 'BRA':'BR', 'CHL':'CL', 'CHN':'CN', 'HKG':'HK', 'COL':'CO',
                 'CZE':'CZ', 'EGY':'EG', 'GRC':'GR', 'HUN':'HU', 'IDN':'ID', 'IND':'IN', 'MEX':'MX',
                 'MYS':'MY', 'PER':'PE', 'PHL':'PH', 'POL':'PL', 'RUS':'RU', 'SAU':'SA', 'THA':'TH',
                 'TUR':'TR', 'TWN':'TW', 'ZAF':'ZA'}

# reduced

citylist = ['ARE_abu-dhabi',
'ARE_dubai',
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
'IDN_jakarta',
'IND_bangalore',
'IND_mumbai',
'IND_new-delhi',
'IND_pune',
'MEX_mexico-city',
'MYS_kuala-lumpur',
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

TTcountry_ids = {'ARE':'AE',  'BRA':'BR', 'CHL':'CL', 'CHN':'CN',
                 'IDN':'ID', 'IND':'IN', 'MEX':'MX', ''
                 'MYS':'MY', 'PHL':'PH', 'POL':'PL', 'RUS':'RU', 'SAU':'SA', 'THA':'TH',
                 'TUR':'TR', 'TWN':'TW', 'ZAF':'ZA'}


outlist=[]
outdict={}
faillist = []
ctryoutdict = {}
ctrylist = []

### 0 bring in 2020 TT data
    
oldTTdf = pd.read_csv('TT_congestion_output_22January2021_103814.csv')
oldTTdf.set_index(oldTTdf.columns[0], inplace = True)
oldTTdf.index = pd.to_datetime(oldTTdf.index, format='%d/%m/%Y')


def TT():
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
    
    #create outdf with a city in it to give structure
    TToutdf = result[result.columns[0]]
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
        TToutdf = pd.concat([TToutdf,workdf], axis = 1)
        TToutdf = TToutdf.rename(columns={"sum": i})
    
    #delete the city we started outdf with
    TToutdf = TToutdf.drop(TToutdf.columns[0], 1)

    ### rename series
    TToutdf = TToutdf.rename(columns=TTcountry_ids)

    #shift date by one day
    TToutdf.index = TToutdf.index + pd.Timedelta(days=6)
    
    ### 5 Output to Excel
    
    #create datetime string for output filename
    now=datetime.now()
    date_time = now.strftime("%d%B%Y_%H%M%S")
    #Create unique name to save the file as
    userfilename='TT_congestion_output_'+date_time+'.csv'
    
#    print(oldTTdf.index)
#    print(TToutdf.index)

    #add NANs for KR
    TToutdf["KR"] = np.nan
    #Change datetime to match
#    TToutdf.index = TToutdf.index.strftime('%d/%m/%Y')

    #combine old and new TT dfs
    xdf = oldTTdf.append(TToutdf)

    xdf = xdf.reindex(dod['driving'].index).fillna(method='ffill')
    
    #add to dataoutdict
    dod['TT'] = xdf
    dodnames.append('TT')
        
    #push df to csv
    xdf.to_csv(userfilename)

#run TT
TT()


##### COVID #####

actualcountrycodes = ['BR', 'CL', 'MX','AE','PL','RU', 'SA', 'TR', 'ZA', 'ID', 'MY', 'PH', 'TH', 'IN', 'TW', 'KR', 'CN']

#reduced
usecountrycodes = ['BRA', 'CHL', 'MEX','ARE','POL','RUS', 'SAU', 'TUR', 'ZAF', 'IDN', 'MYS', 'PHL', 'THA', 'IND', 'TWN', 'KOR', 'CHN']

#from urllib.request import Request, urlopen  # Python 3
#req = Request("https://covid.ourworldindata.org/data/owid-covid-data.csv")
#req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
#content = urlopen(req)

owid_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
coviddf=pd.read_csv(owid_url)

### set index and make index datetime
coviddf.set_index('date', inplace = True)
coviddf.index = pd.to_datetime(coviddf.index)

datas = ['new_cases_smoothed_per_million','new_deaths_smoothed_per_million', 'people_vaccinated_per_hundred']

for datat in datas:
   
    for i in usecountrycodes:
        coviddf1 = coviddf[coviddf['iso_code'] == i]
        
        ### take weekly data
#        covoutdf1 = coviddf1[datat].resample('W').asfreq()
        covoutdf1 = coviddf1[datat]
        ### rename series
        covoutdf1 = covoutdf1.rename(i)
        ### this creates an output df with the first country in the list
        ### in order to have something to merge with
        if i == usecountrycodes[0]:
            covoutdf = covoutdf1
        else:
            ### merge output dataframes into the final
            covoutdf = pd.merge(covoutdf,covoutdf1,how='outer', on='date')
    
    #convert headings to 2 letter country codes
    covoutdf.columns = actualcountrycodes
    
    #sort by date, not sure why needed
    covoutdf.sort_index(axis=0, ascending=True, inplace=True)
    
    #create datetime string for output filename
    now=datetime.now()
    date_time = now.strftime("%d%B%Y_%H%M%S")
    #Create unique name to save the file as
    userfilename='Covid_'+datat+date_time+'.csv'
    userfilename2='Covid_'+datat+'.csv'
    
    
    #push df to csv
    covoutdf.to_csv(userfilename)
    covoutdf.to_csv(userfilename2)
    
    dod[datat] = covoutdf
    dodnames.append(datat)

#### Vaccination Data

glob_peers = ['DEU', 'GBR', 'ISR', 'USA']
readcountrycodes=usecountrycodes + glob_peers
countrycodedict = {'DEU':'DE', 'GBR':'GB', 'ISR':'IL', 'USA':'US', 'ARE':'AE', 'ARG':'AR', 'BRA':'BR', 'CHL':'CL', 'CHN':'CN', 'HKG':'HK', 'COL':'CO',
                 'CZE':'CZ', 'EGY':'EG', 'GRC':'GR', 'HUN':'HU', 'IDN':'ID', 'IND':'IN', 'MEX':'MX',
                 'MYS':'MY', 'PER':'PE', 'PHL':'PH', 'POL':'PL', 'RUS':'RU', 'SAU':'SA', 'THA':'TH',
                 'TUR':'TR', 'TWN':'TW', 'ZAF':'ZA', 'KOR': 'KR'}
countrycodedictrev = {value : key for (key, value) in countrycodedict.items()}

for i in readcountrycodes:
    df1 = coviddf[coviddf['iso_code'] == i]
    ### take weekly data
#        covoutdf1 = coviddf1[datat].resample('W').asfreq()
    vaxoutdf1 = df1['people_vaccinated_per_hundred']
    ### rename series
    vaxoutdf1 = vaxoutdf1.rename(i)
    ### this creates an output df with the first country in the list
    ### in order to have something to merge with
    if i == usecountrycodes[0]:
        vaxoutdf = vaxoutdf1
    else:
        ### merge output dataframes into the final
        ###### THIS WASN'T WORKING WITH MERGE ON OUTER BCOS WAS CREATING A LOAD OF ROWS OF NANS
        ###### AT THE BOTTOM AFTER THE LATEST DATA
        ###### MERGE ON LEFT WORKS BETTER
        vaxoutdf = pd.merge(vaxoutdf,vaxoutdf1,how='left', on='date')

###### NEED TO MAKE FIRST ROW ALL ZEROS
###### THEN WE CAN FFILL AND THE NANS BEFORE VAX STARTS WILL BE ZEROS


# find first row and set to 0
x = vaxoutdf.index[0]
for i in vaxoutdf.columns:
    vaxoutdf[i][x] = 0


# ffill
vaxoutdf = vaxoutdf.fillna(method='ffill')

### Reducing vax data to the start of vaccination period 

row_loc = vaxoutdf.index.get_loc('2020-12-10')
reduced_vacc_df = vaxoutdf.drop(vaxoutdf.index[range(row_loc)])


### Regional and Global Peers
## Grabbing the latest data 
latest_row = vaxoutdf.tail(1)
actualcountrycodes = ['BR', 'CL', 'MX','AE','PL','RU', 'SA', 'TR', 'ZA', 'ID', 'MY', 'PH', 'TH', 'IN', 'TW', 'KR', 'CN']

### Establishing regional and global peers
peer_gs = [['BR', 'CL', 'MX', 'ZA', ],
           ['AE','SA',],
           ['PL','RU', 'TR',  ],
           ['ID', 'MY', 'PH', 'TH', 'IN'],
           ['TW', 'KR', 'CN']]


for i in actualcountrycodes:
    p_group = [i]
    for j in peer_gs:
        work_peer_g = j.copy()
        if i in work_peer_g:
            work_peer_g.remove(i)
            p_group += (work_peer_g)
        else:
            pass
    p_group_a = []
    for l in p_group:
        p_group_a.append(countrycodedictrev[l])
    p_group_a += glob_peers


##### BLOOMBERG DATA #####

BBdlist = ['eps12f', 'eps21', 'eps22', 'gdp21','locindex','fx']

for BBdata in BBdlist:
    
    def create_BBdf(path,x):
        ### this reads a given worksheet from the source excel
        df = pd.read_excel('Bloomberg_Ests_Dashb_Data_v2.xlsx', sheet_name=path, header = [x])
        return df
    
    #Create df and set index
    bbdf = create_BBdf(BBdata,0)
    bbdf.set_index('Date', inplace = True)
    
    #create CheckTotal and drop where CheckTotal == 0
    bbdf['CheckTotal']= bbdf.iloc[:, :].sum(axis=1)
    bbdf = bbdf[bbdf.CheckTotal != 0]
    bbdf.drop(['CheckTotal'], axis=1)
    
    dod[BBdata] = bbdf
    dodnames.append(BBdata)



##### OUTPUT #####

#This aggregates up by country ready for output

#sample country aggregation
chosen_countries = ['BR', 'CL', 'MX','AE','PL','RU', 'SA', 'TR', 'ZA', 'ID', 'MY', 'PH', 'TH', 'IN', 'TW', 'KR', 'CN']

notfound = pd.DataFrame([])

country_aggdict = {}
fields = dod.keys()
for i in chosen_countries:
    countryagglist = []
    for j in fields:
        try:
            countryagglist.append(dod[j][i])
        except KeyError:
            countryagglist.append(notfound)


    tempdf = reduce(lambda left,right: pd.merge(left,right, left_index=True, right_index=True,how='outer'), countryagglist)
    tempdf.columns = dodnames
    country_aggdict[i] = tempdf

''' 

### INDEX  ###
#create usd index data
for i in chosen_countries:
    usdindexdf = pd.DataFrame(country_aggdict['CN'].locindex/country_aggdict['CN'].fx)
    country_aggdict[i]=pd.merge(country_aggdict[i],usdindexdf, left_index = True, right_index = True,how='outer')
    country_aggdict[i].rename(columns={0: "usdindex"}, inplace=True)

#eliminate NaNs in data series
for i in chosen_countries:
    country_aggdict[i] = country_aggdict[i].fillna(method='ffill')

fx3mchglist =[]
locindex3mlist = []
usdindex3mlist = []
for i in chosen_countries:
    z = country_aggdict[i].index.max()
    y = z + pd.DateOffset(months=-3)
    fx3mchglist.append([i,(country_aggdict[i].loc[y].fx/country_aggdict[i].loc[z].fx)-1])
    locindex3mlist.append([i,(country_aggdict[i].loc[y].locindex/country_aggdict[i].loc[z].locindex)-1])
    usdindex3mlist.append([i,(country_aggdict[i].loc[y].usdindex/country_aggdict[i].loc[z].usdindex)-1])

fx3mchgdf = pd.DataFrame(fx3mchglist)
fx3mchgdf.set_index(0, inplace=True)
fx3mchgdf.rename(columns={1: "3m_fx_chg"}, inplace=True)

locindex3mdf = pd.DataFrame(locindex3mlist)
locindex3mdf.set_index(0, inplace=True)
locindex3mdf.rename(columns={1: "3m_loc_index_chg"}, inplace=True)

usdindex3mdf = pd.DataFrame(usdindex3mlist)
usdindex3mdf.set_index(0, inplace=True)
usdindex3mdf.rename(columns={1: "3m_usd_index_chg"}, inplace=True)

chg3mdf = pd.merge(fx3mchgdf,locindex3mdf, left_index = True, right_index = True,how='outer')
chg3mdf = pd.merge(chg3mdf,usdindex3mdf, left_index = True, right_index = True,how='outer')

chg3mdf = chg3mdf.T


### CHARTING TO PDF ###

def twinaxes(ax1, date, data1, data2, c1, c2, y1, y2):
    ### set up the plot for twin axis line graphs
    ax2 = ax1.twinx()
    ax1.plot(date, data1, color=c1)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(y1)
    ax2.plot(date, data2, color=c2)
    ax2.set_ylabel(y2)
    return ax1, ax2



##this section makes the pdf
pdfname='multipage_pdf_'+datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+'.pdf'

with PdfPages(pdfname) as pdf:
    ###from here is where the loop for charts should go
    for ctry in chosen_countries:
        ctryname = country_names[ctry]
        plotdf = country_aggdict[ctry]

        # Create axes
        fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(8.27,11.69))
        fig.suptitle(ctryname, fontsize=16)
        ax1, ax1a = twinaxes(ax1, plotdf.index, plotdf.new_cases_smoothed_per_million, plotdf.new_deaths_smoothed_per_million, 'r', 'b', 'Cases/m (red)', 'Deaths/m (blue)')
        ax1 = plt.xticks(rotation=45)
        ax2.plot(plotdf.people_vaccinated_per_hundred.loc['2010-12-01':])
        ###start date is hard-coded 
        ax2.set(xlabel='Date', ylabel='percentage of population vaccinated per hundred', title=[i])
        ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
        ax2 = plt.xticks(rotation=45)
#        ax2a = plt.gca()
        latest_vax_df = latest_row[p_group_a]
        ax3.bar(p_group_a, latest_vax_df.iloc[0])
        ax3.set(xlabel='Country', ylabel='Percentage of people vaccinated per hundred', title='') # you can also use latest vax df columns for x axis
        ax3.yaxis.set_major_formatter(mtick.PercentFormatter())
        ax3 = plt.xticks(rotation=45)
        
       # if ctry == 'CN':
        #    ax3, ax3a = twinaxes(ax3, plotdf.index, plotdf.workplaces, plotdf.TT, 'r', 'gold', 'Workplaces (red)', 'Traffic congestion (gold)')
       # else:
       #     ax3, ax3a = twinaxes(ax3, plotdf.index, plotdf.workplaces, plotdf.transit, 'r', 'limegreen', 'Workplaces (red)', 'Transit (green)')
        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()
    
        ### Create axes
        fig, (ax4, ax5, ax6) = plt.subplots(3,1, figsize=(8.27,11.69))
        fig.suptitle(ctryname.join(" 2"), fontsize=16)
        ax4, ax4a = twinaxes(ax4, plotdf.index, plotdf.eps12f, plotdf.gdp21, 'r', 'b', '12mf eps (red)', 'GDP 21 (blue)')
        ax4 = plt.xticks(rotation=45)
        ax5, ax5a = twinaxes(ax5, plotdf.index, plotdf.eps21, plotdf.eps22, 'r', 'limegreen', 'eps 21 (red)', 'eps22 (green)')
        ax5 = plt.xticks(rotation=45)
        ax6, ax6a = twinaxes(ax6, plotdf.index, plotdf.eps21, plotdf.gdp21, 'r', 'gold', 'eps 21 (red)', 'GDP 21 (green)')
        ax6 = plt.xticks(rotation=45)
        pdf.savefig(fig)
        plt.close()


        ### Create axes
        fig, (ax7, ax8, ax9) = plt.subplots(3,1, figsize=(8.27,11.69))
        fig.suptitle(ctryname.join(" 2"), fontsize=16)
        ax7 = plt.subplots(figsize=(5, 5))
        ax7.plot(reduced_vacc_df.index, reduced_vacc_df[i])
        ax7.set(xlabel='Date', ylabel='percentage of population vaccinated per hundred', title=[i])
        ax7.spines['bottom'].set_position('zero')
        ax7.yaxis.set_major_formatter(mtick.PercentFormatter())
        ax7 = plt.xticks(rotation=45)
        ax8, ax8a = twinaxes(ax5, plotdf.index, plotdf.eps21, plotdf.eps22, 'r', 'limegreen', 'eps 21 (red)', 'eps22 (green)')
        ax8 = plt.xticks(rotation=45)
        ax6, ax6a = twinaxes(ax6, plotdf.index, plotdf.eps21, plotdf.gdp21, 'r', 'gold', 'eps 21 (red)', 'GDP 21 (green)')
        ax6 = plt.xticks(rotation=45)
        pdf.savefig(fig)
        plt.close()
'''