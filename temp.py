# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:40:21 2020

@author: jsyme
"""
import os
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter

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

#create an unordered df of weights
weights_raw = [['Abud','Cair','Beij'],[5,1,0.5]]
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


for i in dataf1.columns:
    # if first one then make else append as per TT/ecdc 
    if i == dataf1.columns[0]:
        orddwts = dataf1.iloc[:,0]
    else:
        pass
    ### merge output dataframes into the final
    orddwts = pd.concat([orddwts,weights[i]], axis=1)
    #delete the first column which we used to create it
orddwts.drop(orddwts.columns[0], axis=1, inplace = True)


#g = df.groupby('Date')
#outdf1 = df.value / g.value.transform("sum") * df.wt


newdf = (dataf1 * orddwts)
