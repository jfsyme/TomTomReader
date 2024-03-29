# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 09:26:40 2021

@author: jfsym
"""

import pandas as pd

data = pd.read_csv('tomtom_trafic_index.csv')

countrylist = ['Argentina', 'Brazil', 'Chile','Colombia','Peru','Mexico','United Arab Emirates','Saudi Arabia','Turkey',
               'Greece','Poland','Hungary','Czechia','Russia','South Africa','China','India','Pakistan','Taiwan',
               'South Korea','Indonesia','Malaysia','Thailand','Philippines','Kuwait','Egypt']

outdict = {}

for i in countrylist:
    df1 = data[data['country'] == i]
    #need different treatment if only one city as can't take mean of a pd series
    if len(df1.groupby('city').count()) == 1:
        df1.set_index('date', inplace = True)
        outdict[i] = df1['diffRatio']
    else:
        outdict[i] = df1.groupby("date")['diffRatio'].mean()
    
userfilename='temp_out.csv'

#push df to csv
outdict['Brazil'].to_csv(userfilename)