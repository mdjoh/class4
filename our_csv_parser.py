#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

# if os.path.isfile(myfilename):
#   print("yay, I have a file")
#   if sky == blue:
#     print('yay the sky is blue')
# else:
#   print ('boo, no files for me')

#homework 1
list1=[]

# reach homework
# start with blank lists for each to append to
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
col12 = []
col13 = []
col14 = []

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

    # reach homework
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
        col12.append(list1[11])
        col13.append(list1[12])
        col14.append(list1[13])

    # print newly formed lists
    print(col1)
    print(col2)
    print(col3)
    print(col4)
    print(col5)
    print(col6)
    print(col7)
    print(col8)
    print(col9)
    print(col10)
    print(col11)
    print(col12)
    print(col13)
    print(col14)

    print('finished!')
