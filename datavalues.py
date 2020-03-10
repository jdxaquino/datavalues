#!/usr/bin/env python

#Author: Jose D'Aquino
#Ascription: National Institute of Astrophysics, Optics and Electronics (INAOE)
#Email: jdxaquino@inaoe.mx
#Date: 10/03/20
#Description: Search data values for calculate any math operator

import readcol as rc
import glob
import fnmatch
import os
import ntpath
from datetime import datetime
import matplotlib.pyplot as plt
import math
import numpy as np
import numpy.ma as ma
import pandas as pd

#Coordenates: Longitude, Latitude in the file
axis1 = [[4, 21], [4, 22],
        [5, 20], [5, 21], [5, 22],
        [6, 17], [6, 18], [6, 19], [6, 22],
        [7, 17], [7, 18], [7, 21],
        [8, 15], [8, 16], [8, 17], [8, 19], [8, 20], [8, 21],
        [9, 14], [9, 15], [9, 18], [9, 19], [9, 20], [9, 21],
        [10, 13], [10, 14], [10, 18], [10, 19], [10, 20], [10, 21],
        [11, 16], [11, 17], [11, 18], [11, 19], [11, 20], [11, 21],
        [12, 15], [12, 16], [12, 17], [12, 18], [12, 19], [12, 20], [12, 21],
        [13, 14], [13, 15], [13, 16], [13, 17], [13, 18], [13, 19], [13, 20], [13, 21],
        [14, 13], [14, 14], [14, 15], [14, 16], [14, 17], [14, 18], [14, 19], [14, 20], [14, 21],
        [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [15, 15], [15, 16], [15, 17], [15, 18], [15, 19], [15, 20],
        [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [16, 15], [16, 16], [16, 17], [16, 18], [16, 19],
        [17, 9], [17, 10], [17, 11], [17, 12], [17, 13], [17, 14], [17, 15], [17, 16], [17, 17], [17, 18], [17, 19],
        [18, 8], [18, 9], [18, 10], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15], [18, 16], [18, 17], [18, 18], [18, 19],
        [19, 8], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18], [19, 19],
        [20, 7], [20, 8], [20, 9], [20, 10], [20, 11], [20, 12], [20, 13], [20, 14], [20, 15], [20, 16], [20, 17], [20, 18],
        [21, 7], [21, 8], [21, 9], [21, 10], [21, 11], [21, 12], [21, 13], [21, 14], [21, 15], [21, 16],
        [22, 7], [22, 8], [22, 9], [22, 10], [22, 11], [22, 12], [22, 13], [22, 14], [22, 15], [22, 16],
        [23, 6], [23, 7], [23, 8], [23, 9], [23, 10],
        [24, 6], [24, 7], [24, 8], [24, 9], #53
        [25, 7], [25, 8],
        [26, 6], [26, 7], [26, 8],
        [27, 6], [27, 7], [27, 8],
        [28, 6], [28, 7], [28, 8], 
        [29, 8], [29, 9],
        [30, 8], [30, 9], [30, 10], [30, 11],
        [31, 8], [31, 9], [31, 10], [31, 11],
        [32, 9], [32, 10], [32, 11],
        [33, 11]] #183 points

axis2 = [[1, 14], [1, 15],
        [2, 10], [2, 11], [2, 13], [2, 14],
        [3, 10], [3, 11], [3, 12], [3, 13], [3, 14],
        [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12],
        [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12],
        [6, 4], [6, 5], [6, 6],
        [7, 4], [7, 5],
        [8, 6], [8, 7]] #33 points

matches = []
for root, dirnames, filenames in os.walk('/home/user/directory/data/2018'):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))
for root, dirnames, filenames in os.walk('/home/user/directory/data/2019'):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))
for root, dirnames, filenames in os.walk('/home/user/directory/data/2020'):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))

e = open("/home/user/directory/data/name-file.dat","w+")
f = open("/home/user/directory/data/name-file2.dat","w+")
g = open("/home/user/directory/data/name-file3.dat","w+")

date_max = []
date_avg = []
date_min = []
value_max = []
value_avg = []
value_min = []
for filename in matches:
    name = ntpath.basename(filename)
    if not 'STEC' in name:
        data = []
        values = rc.fgetcols(filename)
        datat = np.array(values)
        if len(datat) <= 10:
            axis = axis2
        else:
            axis = axis1
        for i in range(0,len(datat)):
            for j in range(0,len(datat[i])):
                if [i,j] in axis:
                    date = float(datat[i,j])
                    data.append(date)
        if len(data) > 0:
            maximum = max(data)
            average = sum(data)/len(data)
            minimum = min(data)
            print 'Maximum:', maximum
            print 'Average:', average
            print 'Minimum:', minimum
            if maximum <= 8000 and not math.isnan(maximum):
                value_max.append(maximum)
                strtime = name[12:27]
                datetime_object = datetime.strptime(strtime, '%Y%m%dT%H%M%S')
                date_max.append(datetime_object)
                e.write(name + " " + str(maximum) + "\n")
                    
            if average <= 8000 and not math.isnan(average):
                value_avg.append(average)
                strtime = name[12:27]
                datetime_object = datetime.strptime(strtime, '%Y%m%dT%H%M%S')
                date_avg.append(datetime_object)
                f.write(name + " " + str(average) + "\n")
                            
            if minimum <= 8000 and not math.isnan(minimum):
                value_min.append(minimum)
                strtime = name[12:27]
                print filename
                datetime_object = datetime.strptime(strtime, '%Y%m%dT%H%M%S')
                date_min.append(datetime_object)
                g.write(name + " " + str(minimum) + "\n")
e.close()
f.close()
g.close()
plt.plot(date_max, value_max,'bo', label = 'MAXIMUM VALUES')
plt.plot(date_avg, value_avg,'go', label = 'AVERAGE VALUES')
plt.plot(date_min, value_min,'ro', label = 'MINIMUM VALUES')
plt.legend(loc = 2)
plt.title('Data Values Plot')
plt.xlabel('TIME')
plt.ylabel('TECU ($10^{16} electrons*m^{-2}$)')
plt.grid()
plt.show()
