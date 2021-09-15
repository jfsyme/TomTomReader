# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:07:01 2021

@author: hboateng
"""

import pandas as pd 

tomtom_githuburl = 'https://raw.githubusercontent.com/jfsyme/COVID19_mobility/master/tomtom_reports/tomtom_trafic_index.csv'

countrylist = ['Argentina', 'Brazil', 'Chile','Colombia','Peru','Mexico','United Arab Emirates','Saudi Arabia','Qatar','Turkey',
               'Greece','Poland','Hungary','Czechia','Russia','South Africa','China','India','Pakistan','Taiwan',
               'South Korea','Indonesia','Malaysia','Thailand','Philippines']


df = pd.read_csv(tomtom_githuburl)
df1 = df[df['country'].isin(countrylist)]
groupeddf = df1.groupby('city')['congestion'].mean()
print(groupeddf.head())


ttdf = pd.read_csv(tomtom_githuburl)
ttdf.set_index('date', inplace=True)
ttdf1 = ttdf[ttdf['country'].isin(countrylist)]
ttdf2= ttdf1.groupby(['country','city'], as_index=False).mean()
ttdf2.drop(['diffRatio'], axis=1, inplace=True)