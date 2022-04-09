#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 08:34:40 2022

@author: thangdnsf

Basic data strucrure in python:
    - List 
    - Set
    - Dict
    - Map
"""

# List:
datalist  = [1,2,3,4,5,6]

## task 1: add 5 in each data item in datalist
## approach 1:
for i in range(len(datalist)):
    datalist[i] += 5

## approach 2: for loop in array
datalist = [data + 5 for data in datalist]

## task 2: append a dataitem into list
datalist + [5]
datalist.append(5)
datalist.extend([5])

import numpy as np
datalist_np = np.array(datalist)
datalist_np + 5
datalist_np.shape

matrix = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
np.sum(matrix)
np.sum(matrix,axis=0)
np.sum(matrix,axis=1)
matrix[1:3, 1:3]
# 1:3 ~ range(1,3)
matrix[1:, 1:]
matrix[:2, :2]

matrix2 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
# inner product
matrix*matrix2

np.dot(matrix, matrix2)
matrix.dot(matrix2)

matrix.T
np.mean(matrix)
try:
    print(thang)
except:
    print("Chua define be oi")
# Set 
a = {1,2,4,2,3,5}
b = {2,7,9,1}

a & b
a | b
a - b
b - a
a^b # (a | b) - (a & b)

1 in datalist

# Dict

studentdict = {
    'A22852' : "NGUYEN DUC THANG",
    'A12345' : "NGUYEN THI A",
    'A67863' : "DANG VAN B",
    1: 2,
    3: 4
    }

studentdict.keys()
studentdict.values()

for i, (key,value) in enumerate(studentdict.items()):
    print(f"{i}, {key} : {value}")

studentdict['muaxuanhoano'] = 'laviem'
del studentdict['A22852']
