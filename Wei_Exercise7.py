#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:08:32 2018

@author: Alicia
"""
import pandas as pd
#below is a csv on my computer. will need to change 
iris_data = pd.read_csv('/Users/Alicia/Desktop/Fall/BIOS60318/Exercise6/IBC_EX6/iris.csv') #will need to change file path according to whatever file you want to return odd rows of

##########
#Problem1#
##########
def problem_one(x):
   return x.iloc[1::2] #this returns the odd rows
print problem_one(iris_data)

##########
#Problem2#
##########

##Part1##
def flowers(Species,data):
    count = 0
    for flower in range(len(data.iloc[:,4])): #range tells flowers we'll be using numbers in flower. #len: length of list #data.iloc[:,4]: all rows, pick one column
        if data.iloc[flower,4] == Species: #itterations through individual rows. a logic check
            count += 1 #if above is true, count increases by one
    return count
print flowers('setosa',iris_data) #Usage: Change 'setosa' with flower name as needed


##Part 2##
def sepalWidth(data,width):
    data2 = data[data["Sepal.Width"] > width]
    return data2
print sepalWidth(iris_data,3) #Usage: Change 3 for desired width

##Part 3##
def flowerFile(flower,data):
    data3 = data[data["Species"]==flower]
    data3.to_csv(flower+".csv",sep=',')
flowerFile('setosa',iris_data) #Usage: Change setosa name to other flower names as needed as needed