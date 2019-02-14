#!/usr/bin/env python

import os
import numpy as np
import argparse

# homework 1
# open diabetes data file
myfilename = "diabetes_data.txt"

# start with empty list for cleaned values to concatenate to
list1=[]

# start with empty lists for each to append to
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
col10 = []
col11 = []

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')

        # homework 1
        for value in values:
            try:
                list1+=[int(value)]
            except:
                list1+=[float(value)]

        print(list1)

        # append elements to list of specified column
        col1.append(list1[0])
        col2.append(list1[1])
        col3.append(list1[2])
        col4.append(list1[3])
        col5.append(list1[4])
        col6.append(list1[5])
        col7.append(list1[6])
        col8.append(list1[7])
        col9.append(list1[8])
        col10.append(list1[9])
        col11.append(list1[10])
    
    # print newly formed lists
    #print(col1)
    #print(col2)
    #print(col3)
    #print(col4)
    #print(col5)
    #print(col6)
    #print(col7)
    #print(col8)
    #print(col9)
    #print(col10)
    #print(col11)

# put "cleaned" data in one array
data = np.array([[col1], [col2], [col3], [col4], [col5], [col6], [col7], [col8], [col9], [col10], [col11]])

# calculate and print means and std. devs
means = np.mean(data, axis=0)
stdevs = np.std(data, axis=0)

print(means)
print(stdevs)
