# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:12:49 2020

@author: James
"""

import os
from datetime import datetime
from TTreaderfunc import TTreader
import csv

##this is the handler to manage all the TomTom 

#create datetime string for output filename
now=datetime.now()
date_time = now.strftime("%d%B%Y_%H%M%S")

print(date_time)


#working directory
corelocation='C:\\Users\\James\\Documents\\Python Scripts\\tomtoms\\TT_core\\'

#Sets the scripts working directory to the location of the screenshots
os.chdir(corelocation)

#Create unique name to save the file as
userfilename='TT_output_'+date_time+'.csv'

print(userfilename)

#Get all the city screenshot filenames
citylist = []
for filename in os.listdir('.'):
    l = len(filename)
    typ = filename[l-3:l]
    if typ == 'PNG' or typ == 'png':
        citylist.append(filename)
    else:
        pass

citytraff = []
#retrieve traffic
for f in citylist:
    citytraff.append([f, TTreader(f)])

print(citytraff)

#output filenames to csv as test
    
with open(userfilename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(citytraff)

