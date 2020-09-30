# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:40:21 2020

@author: jsyme
"""
from datetime import datetime
import pandas as pd

#dummy dataset
datas = [['Date','Abud','Beij','Cair'],['31-Dec-2019',1,2,3],
         ['31-Jan-2020',10,20,30],['29-Feb-2020',100,200,300]]
dataf1 = pd.DataFrame(datas)

#set header and set index to date
new_header = dataf1.iloc[0] 
dataf1 = dataf1[1:] 
dataf1.columns = new_header 
dataf1.set_index('Date', inplace = True)
dataf1.index = pd.to_datetime(dataf1.index)
dataf1.index = dataf1.index.date

#dummy weights set in different order
weights_raw = [['Abud','Cair','Beij'],[5,1,0.7]]
#create an unordered df of weights
weight = pd.DataFrame(weights_raw)
new_header = weight.iloc[0] 
weight = weight[1:] 
weight.columns = new_header 

#copy weights down to same length as data
weights = pd.concat([weight]*len(datas), ignore_index=True)
weights = weights[1:]
#create a date column and set it as the index
weights['Date'] = dataf1.index
weights.set_index('Date', inplace = True)

#create empty dataframe and add weights in same column order as in data
orddwts = pd.DataFrame([])
for i in dataf1.columns:
    orddwts = pd.concat([orddwts,weights[i]], axis=1)

#multiply data by weights
wtddata = (dataf1 * orddwts)

#sum weighted data and weights
wtddata['sum'] = wtddata.sum(axis = 1)
orddwts['sum'] = orddwts.sum(axis = 1)

outdf = wtddata['sum'] / orddwts['sum']

    