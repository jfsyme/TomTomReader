# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:40:11 2020

@author: James
"""


import numpy as np
import matplotlib.pyplot as plt
import imageio
import statistics
import csv

#import graph shape
im = imageio.imread('C:\\Users\\James\\Documents\\Python Scripts\\AD_7.png')

#determine shape
h = im.shape[0]
w = im.shape[1]

#256 rows, 1221 columns, white pixels are 255,255,255
#vert rows are [221 221 221 255]
# ? [255 31 12 255]
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
    x = im[0][c][0:3]
    if np.all(x > 210) and np.all(x < 235):
        print('vert row at column',c)
        v1 = c
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
            print('horiz 140 row at row',r)
            h140 = r
        elif h140 != 1000 and h130 == 1000 and r > (h140 + 4):
            print('horiz 130 row at row',r)
            h130 = r
        elif h130 != 1000 and h120 == 1000 and r > (h130 + 4):
            print('horiz 120 row at row',r)
            h120 = r
        elif h120 != 1000 and h110 == 1000 and r > (h120 + 4):
            print('horiz 110 row at row',r)
            h110 = r
        elif h110 != 1000 and h100 == 1000 and r > (h110 + 4):
            print('horiz 100 row at row',r)
            h100 = r
        else:
            pass
    else:
        pass

#4 impute 0%
h0 = int(((h120-h140) * 6.5)+ h130)
print('horiz 0 row (x-axis) at row',h0)

#5 find start of horiz bar
for i in range(v1,0,-1):
    x = im[h140][i][0:3]
    if np.all(x < 250):
        pass
    else:
        v0 = i
        break
print('start of data at column',v0)

#6 find end of horiz bar
for i in range(v1,w):
    x = im[h140][i][0:3]
    if np.all(x < 250):
        pass
    else:
        vmax = i
        break
print('start of data at column',vmax)
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
        vmaxred = c
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
    for r in range (h110+5               ,h0):
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

print(bluetemp[0:20])

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


#10 generate data
#11 store data


#movavg
'''
newbluelist = bluelist.copy()
for i in range(len(newbluelist)):
    if i < 51:
        newbluelist[i] = 0
    else:
        newbluelist[i] = sum(bluelist[i-2:i])/3
'''


plt.plot(redlist, color='red')
#plt.ylabel('some numbers')
#plt.show()

plt.plot(bluelist)
#plt.ylabel('some numbers')
plt.show()

'''

#find axis
for i in range (238):
    rowscore = []
    for j in range (867):
        rowscore.append(statistics.mean(im[i][j]))

checkcolumns=[]
for i in range (4,867):
    if statistics.mean(rowscore[i-4:i])<80 and statistics.mean(rowscore[i:i+4])<80:
        if (i-1) in checkcolumns or (i-2) in checkcolumns:
            pass
        else:
            checkcolumns.append(i)

#print(checkcolumns)
#print(len(checkcolumns))


imvals = []
for i in range(1264):
    for j in range(768):
        columnlook = statistics.mean(im[j][i][:3])
        axislook =  statistics.mean(im[767][i][:3])
        if columnlook >80:
            pass
        else:
            columnval = [j,axislook,i]
            imvals.append(columnval)
            break

print(imvals)

with open('ml_quant_survey.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(imvals)

csvFile.close()
        
'''
    


    
            
    

