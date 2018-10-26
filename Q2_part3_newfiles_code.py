#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 00:01:43 2018

@author: ColinSheehan
"""

def newfilefunc(filename, string): #filename in quotes and define string as species names included in file prior to running function
    iris=pd.read_csv(filename)
    for animal in string:
        critter=iris[iris.Species==animal]
        newfile=animal+'.csv'
        import sys
        sys.stdout = open(newfile, 'w')
        print(critter)  
#I ran the function as:
#  >string = ["setosa", "virginica", "versicolor",]
#  >newfilefunc("iris.csv", string)