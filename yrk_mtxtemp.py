# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:17:17 2023

@author: jfsym
"""
from random import randint, random

season = 2
workers = 10
flooded_dict = {0:0, 1:0, 2:0}

mtxp_dict= {0:'\u0020', 1:'\u2588', 2:'\u007C', 3:'\u2584',
            4:'\u259E', 5:'\u21D1', 6:'\u2590'}


def matrixprinter(m):
    linestring = '      YELLOW RIVER KINGDOM  \n'
    for i in m:
        for j in i:
            linestring += str(mtxp_dict[j])
        linestring +=' \n'
    linestring +="   DYKE        VILLAGES      MOUNTAINS"
    print(linestring)
    
def setup():
    #0 space  \u0020  
    #1 thick block \u2588 #219
    #2 vert line \u007C #221
    #3 bottom right check \u2584 #220
    #4 czech check \u259E #165
    #5 up arrow \u21D1 #138
    #6 bottom right block \u275A #222
    
    
    #40x25
    #actually 40x23
    
    #create 40x23 block of 0s
    mtxline = []
    for i in range(40):
        mtxline.append(0)
    mtx = []
    for i in range(23):
        mtx.append(mtxline.copy())
    
    #print river, dyke
    for i in range(23):
        mtx[i][0] = 1
        mtx[i][2] = 2
        mtx[i][3] = 2
    
    #print mountains
    for i in range(2,20,2):
        mtx[i][28] = 6
        mtx[i+1][27] = 3
        mtx[i+1][28] = 1
        mtx[i+1][29] = 1
        mtx[i+1][30] = 3
        mtx[i+1][33] = 6
        mtx[i+2][32] = 3
        mtx[i+2][33] = 1
        mtx[i+2][34] = 1
        mtx[i+2][35] = 3
    
    village_list = [(12,8), (20,12), (21,18)]
    
    for i in village_list:
        mtx[i[1]][i[0]-1] = 5
        mtx[i[1]][i[0]] = 4
        mtx[i[1]+1][i[0]-1] = 4
        mtx[i[1]+1][i[0]] = 5

    return mtx

def flood(mtx):
    #Flood severity.
    fs=0
    if season == 1:
        fs = randint(1,330) / (workers + 1)
    elif season ==2:
        fs = (randint(1,100) + 60) / (workers + 1)
    elif season == 3:
        return
    else:
        print ("Unknown season " + str(season))
    if fs < 1:
        return
    elif fs < 2:
        fs2 = 2* random()
    else:
        fs2 = 4 * random()

    floodx = 5
    floody = randint(1,8) + 10
    #    Local k, key = -1, v, w1, w2
    for k in range(int(fs2*(100))):
        floodcase = randint(1,4)
        if floodcase == 1 and floodx < 24:
            floodx += 1
        elif floodcase == 2 and floodx > 5:
            floodx = floodx -1
        elif floodcase == 3 and floody < 21:
            floody +=1
        elif floodcase == 4 and floody > 2:
            floody = floody -1
        else:
            pass
        mtx[floody][floodx] = 1

mtx = setup()
flood(mtx)


'''
def flood():
    #Flood severity.
    fs=0
    if season == 1:
        fs = randint(1,330) / (workers + 1)
    elif season ==2:
        fs = (randint(1,100) + 60) / (workers + 1)
    elif season == 3:
        return
    else:
        print ("Unknown season " + str(season))
    
    if fs < 1.0:
        return
    
    was_flooded = 1
    
    floodx = 5
    floody = randint(1,8) + 10
#    Local k, key = -1, v, w1, w2
    for k in range(100):
        floodcase = randint(1,4)
        if floodx < 24:
            floodx += 1
        elif floodx > 5:
            floodx = floodx -1
        elif floody < 21:
            floody +=1
        elif floody > 2:
            floody -=1
        else:
            pass
        mtx[floody][floodx] = 1

    # Have any of the villages flooded ?
    For v = 1 To 3
      w1 = vx(v) - x
      w2 = y - vy(v)
      If w2 = 0 Or w2 = 1 Then
        If w1 = 0 Or w1 = 1 Then flooded(v) = 1 : Inc num_flooded
        If w1 = -1 Then Exit For
      EndIf
    Next
    
'''
    
matrixprinter(mtx)

