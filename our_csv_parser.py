#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

# if os.path.isfile(myfilename):
#   print("yay, I have a file")
#   if sky == blue:
#     print('yay the sky is blue')
# else:
#   print ('boo, no files for me')

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
                int(value)
            except:
                float(value)

        print(values)

    # reach homework
        # append elements to list of specified column
        col1.append(values[0])
        col2.append(values[1])
        col3.append(values[2])
        col4.append(values[3])
        col5.append(values[4])
        col6.append(values[5])
        col7.append(values[6])
        col8.append(values[7])
        col9.append(values[8])
        col10.append(values[9])
        col11.append(values[10])
        col12.append(values[11])
        col13.append(values[12])
        col14.append(values[13])

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
