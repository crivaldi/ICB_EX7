#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:20:12 2018

@author: ColinSheehan
"""

string = ["setosa", "virginica", "versicolor",]
def observation_function(filename, string): #put filename in quotes and define string of the species names included in file prior to running function
    iris=pd.read_csv(filename)
    for animal in string:
        critter=iris[iris.Species==animal]
        species=critter.iloc[:,4]
        num = len(species)
        print("number of observations for,", animal, ":", num)
# I ran the function as: 
# >string = ["setosa", "virginica", "versicolor",]
# >observation_function("iris.csv", string)