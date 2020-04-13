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
        else:
            pass
    else:
        pass

#4 impute 0%
h0 = int(((h120-h140) * 6.5)+ h130)
print('horiz 0 row (x-axis) at row',h0)

#5 read across to second full vert bar
#6 impute end column
#6.5 find start???
#7 scan for red line
#8 scan for blue line
#9 infill blue line
#10 generate data
#11 store data

#for r in range (256):
#    print(im[r][300])

#samp = im[0][0:1220]
samp = im[0:256][125]

#for i in range(256):
#    if np.all(samp[i] > 254):
#        pass
#    else:
 #   print(i, samp[i])
    

#loop through array
#for i in range ():
#    for j in range (866):
redlist = []
for c in range (1221):
    red = 0
    for r in range (256):
        x = im[r][c]
        if np.any(x < 50) and red == 0:
            red +=1
            redspot = r
        else:
            pass
    if red > 0:
        redlist.append(255-redspot)
    else:
        redlist.append(0)

bluelist = []
for h in range (1221):
    blue = 0
    for i in range (256):
        x = im[i][h]
        if np.any(x < 180) and np.all(x > 100) and blue == 0:
            blue +=1
            bluespot = i
        else:
            pass
    if blue > 0:
        bluelist.append(255-bluespot)
    else:
        bluelist.append(0)

#pickl up gaps in dotted line
for i in range(len(bluelist)):
    if i < 51:
        bluelist[i] = 0
    else:
        if bluelist[i] < 40 :
            bluelist[i] = bluelist[i-1]
        else:
            pass

#movavg
newbluelist = bluelist.copy()
for i in range(len(newbluelist)):
    if i < 51:
        newbluelist[i] = 0
    else:
        newbluelist[i] = sum(bluelist[i-2:i])/3



plt.plot(redlist)
#plt.ylabel('some numbers')
plt.show()

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
    


    
            
    

