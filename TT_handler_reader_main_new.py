# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:12:49 2020

@author: James
"""

import os
from datetime import datetime
#import csv
import pandas as pd
import numpy as np
import imageio

def TTreader(fname):
    
    #import graph shape
    im = imageio.imread(fname)
    
    #determine shape
    h = im.shape[0]
    w = im.shape[1]
    print('height:',h)
    print('width:',w)
    
    #white pixels are [255,255,255]

    #vert rows are [221 221 221 255]

    # horiz row [238 238 238 255] [240, 240, 240, 255]

    #red line [255,  86,  72, 255] [255,  87,  73, 255]
    
    #blue dash [164, 197, 232, 255]
    
    #blue dot [  0,  75, 126, 255]
    
    #yellow dot [253, 197,  48, 255]
    
    #text [102, 102, 102, 255]
    
    
    #screenshot specification
    #taken above the 140% horiz line but intersecting with vert 
    #taken to the left of y axis numbers
    #taken below times
    #taken to the right of now
    
    #1 read across, find starting vert bar
    #2 read down to 100%
    #3 read down to 90%
    #4 impute 0%
    #5 read across to second full vert bar
    #6 impute end column
    #7 scan for red line
    #8 scan for blue line
    #9 infill blue line
    #10 generate data
    #11 store data
    
    #1 read across, find starting vert bar
    for c in range (w):
        vx = im[0][c][0:3]
        if np.all(vx > 210) and np.all(vx < 235):
            v1 = c
            print('v1:',v1)
            break
        else:
            pass
    
    
    #2 read down to 140% and 130%
    #repetition here, push to dictionary?
    
    c = v1-2
    h140 = 1000
    h130 = 1000
    h120 = 1000
    h110 = 1000
    h100 = 1000
    for r in range (h):
        x = im[r][c][0:3]
        if np.all(x > 235) and np.all(x < 250):
            if h140 == 1000:
                h140 = r
                print('h140:',h140)
            elif h140 != 1000 and h130 == 1000 and r > (h140 + 4):
                h130 = r
            elif h130 != 1000 and h120 == 1000 and r > (h130 + 4):
                h120 = r
            elif h120 != 1000 and h110 == 1000 and r > (h120 + 4):
                h110 = r
            elif h110 != 1000 and h100 == 1000 and r > (h110 + 4):
                h100 = r
                print('h100:',h100)
            else:
                pass
        else:
            pass

    #this is if horiz lines don't extend left of v1 line
    if h140 == 1000:
        for c in range (v1+10,w,1):
            vx = im[0][c][0:3]
            if np.all(vx > 210) and np.all(vx < 235):
                v2 = c
                print('v2:',v2)
                break
            else:
                pass
        c = v2-2
        h140 = 1000
        h130 = 1000
        h120 = 1000
        h110 = 1000
        h100 = 1000
        for r in range (h):
            x = im[r][c][0:3]
            if np.all(x > 235) and np.all(x < 250):
                if h140 == 1000:
                    h140 = r
                    print('h140:',h140)
                elif h140 != 1000 and h130 == 1000 and r > (h140 + 4):
                    h130 = r
                elif h130 != 1000 and h120 == 1000 and r > (h130 + 4):
                    h120 = r
                elif h120 != 1000 and h110 == 1000 and r > (h120 + 4):
                    h110 = r
                elif h110 != 1000 and h100 == 1000 and r > (h110 + 4):
                    h100 = r
                    print('h100:',h100)
                else:
                    pass
        else:
            pass
    else:
        pass
    
    #4 impute 0%
    h0 = int(((h100-h140) * 2.5)+ h100)
    print('h0:',h0)
    
    
    
    #5 find start of horiz bar
    for k in range(v1,1,-1):
        x = im[h140][k][0:3]
        if np.all(x < 250):
            pass
        else:
            v0 = k
            print('v0:',v0)
            break
    
    vmax = w
    #6 find end of horiz bar
    for i in range(v1,w):
        x = im[h100][i][0:3]
        if np.all(x < 253):
            pass
        else:
            vmax = i
            break
    ###this isn't right
    
    
    #7 scan for red line
    redlist = []
    for c in range (v0+2,vmax):
        red = 0
        for r in range (h):
            x = im[r][c]
            if np.any(x < 50) and red == 0:
                red +=1
                redspot = r
            else:
                pass
        if red > 0:
            redlist.append(((redspot-h0)/(h100-h0)))
        else:
            break
    #clean for red now circle
    y = len(redlist)
    #circ = (redlist[y-6]+redlist[y-1])/2
    del redlist[y-6:y]
    vmaxact = (len(redlist)+v0+2)
    
    
    
    #8 scan for blue line
    #blue dash [164, 197, 232, 255]
    bluelist = []
    bluetemp = []
    for c in range (v0+2,vmaxact):
        blue = 0
        for r in range (h110+5,h0):
            x = im[r][c][0:3]
    #        if np.any(x < 200) and np.all(x > 150) and blue == 0:
            if (x[2] > 220) and (x[0] < 180) and (x[0] > 140) and blue == 0:
                blue +=1
                bluespot = r
            else:
                pass
        if blue > 0:
            bluetemp.append(bluespot)
            bluelist.append(((bluespot-h0)/(h100-h0)))
        else:
            bluelist.append(999)
            bluetemp.append(999)
        
    #9 infill blue line
    b0 = 0
    #This is the first element of bluelist with a dash
    
    #Can't forwardfill if first element is 999
    for i in range(len(bluelist)-1):
        if bluelist[i] == 999:
            pass
        else:
            b0 = i
            break
    
    #if first element <> 999, ignore, otherwise bfill
    if b0 == 0:
        pass
    else:
        for i in range (b0,0,-1):
            bluelist[i] = bluelist[i+1]
    
    #now ffill
    for i in range(len(bluelist)):
        if bluelist[i] == 999:
            bluelist[i] = bluelist[i-1]
        else:
            pass
    #lastcheck
    for i in range(len(bluelist)):
        if bluelist[i] == 999:
            bluelist[i] = redlist[i]
        else:
            pass
    fn = fname[0:len(fname)-9]
    bl=[fn+'_blue']
    bl+=bluelist
    rl=[fn+'_red']
    rl+=redlist
    
    ll=[rl,bl]

    return (ll)

##this is the handler to manage all the TomTom 

#create datetime string for output filename
now=datetime.now()
date_time = now.strftime("%d%B%Y_%H%M%S")

print(date_time)


#working directory
corelocation='C:\\Users\\jsyme.JOHCM\\Documents\\Q_Macro\\tomtoms\\TTcore_1807\\'

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
    print(f)
    #citytraff.append([f, TTreader(f)])
    citytraff += TTreader(f)


#output filenames to csv as test
    
#list of lits to dataframe
df = pd.DataFrame(citytraff)

#transpose so that data runs in columns
df= df.transpose()

#set first row to be column labels
df.columns = df.iloc[0]

#delete first row as it  still holds dataset names
df = df.drop(df.index[0])

#push df to csv
df.to_csv(userfilename)

