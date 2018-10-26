#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:38:28 2018

@author: ColinSheehan
"""

def sepalfunc(filename, width): #filename in quotes and width is input for desired sepal width to test against
    iris=pd.read_csv(filename)
    lis = len(iris)
    for num in range(0, lis):
        interest = iris.iloc[num, 1]
        row = iris.iloc[num, :]
        if interest > width:
            print(row)
#I ran the function as:
# >sepalfunc("iris.csv", 4.0)    