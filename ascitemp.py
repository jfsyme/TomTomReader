# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:28:49 2023

@author: jfsym
"""
from random import randint
'''
print('2584 \u2584') #220
print('259E \u259E') #165
print('2588 \u2588') #219
print('21D1 \u21D1') #138
print('275A \u275A') #222
print('007C \u007C') #221
'''
village_list = [(12,8), (20,12), (21,18)]

class village:
  def __init__(self, name, popn, xloc, yloc, isattack, isflood):
    self.name = name
    self.popn= popn
    self.xloc = xloc
    self.yloc = yloc
    self.isattack = isattack
    self.isflood = isflood

v1 = village("Atown", 36, 12, 8, 0, 0)
v2 = village("Bville", 48, 20, 12, 0, 0)

for i in village_list:
    print(i)
    print(i[0]-1,i[1])
    print(i[0],i[1])
    print(i[0]-1,i[1]+1)
    print(i[0],i[1]+1)

fs2 = 2

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
#    print ('a', floodx, floody)
    for i in village_list:
        if i[0] - floodx == 0 or i[0] - floodx == 1:
            if i[1] - floody == 0 or i[1] - floody == -1:
                print((floodx, floody), i)
            else:
                pass
        else:
            pass
    