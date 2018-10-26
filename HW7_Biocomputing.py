# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:14:42 2018

@author: Alexis
"""

import pandas as pd

#problem 1    
def OddRowFunction(filename): #returns rows that are odd from file
    iris_data=pd.read_csv(filename)
    OddDF=iris_data.iloc[1: :2,:]#interval through rows by 2
    return OddDF

ResultDF=OddRowFunction('iris.csv')
print(ResultDF)
#problem 2
def SpeciesOccurence(Species):
    iris_data=pd.read_csv('iris.csv')
    SpeciesRows=iris_data[iris_data.Species==Species]#gets rows with that species
    NumofRows=SpeciesRows.shape[0]#takes the number of rows
    return NumofRows

SetosaOccur=SpeciesOccurence('setosa')
print "The number of occurances for Setosa is",SetosaOccur
def SepalWidthGreaterThan(WidthValue):
    iris_data=pd.read_csv('iris.csv')
    SepalWidthGreaterRows=iris_data[iris_data['Sepal.Width']>WidthValue]#gets rows with width greater
    return SepalWidthGreaterRows

SepalWidthGreater4_1=SepalWidthGreaterThan(4.1)
print(SepalWidthGreater4_1)
def DataSpecies_CSV(Species):
    iris_data=pd.read_csv('iris.csv')
    SpeciesRows=iris_data[iris_data.Species==Species] #takes a species as input
    SpeciesRows.to_csv(Species+'.csv', sep=',',index=False) #creates csv file with specific name
    return 0

DataSpecies_CSV('versicolor')



 