#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:31:11 2018

@author: mlpoterek
"""

from pandas import DataFrame, read_csv
import pandas as pd

#The file used to create a dataframe and test the functions
location = r'/Users/mlpoterek/Biocomp/ICB_EX7/iris.csv'
df = pd.read_csv(location)

#Problem 1:

#Return the odd rows of a dataframe
def odd_rows(dataframe):
    return dataframe.iloc[1::2] #prints every second row starting at line 1
    
#Problem 2:
    
#Return the number of observations of a given species
def spec_count(dataframe):
    return dataframe['Species'].value_counts()

#Return the rows with Sepal.Width > a value specified by the user
def sepal_size(dataframe, width):
    return dataframe[dataframe['Sepal.Width'] > width]  

#Write the data for a given species to a comma delimited file with the
#given species name as the file name 
def spec_file(dataframe, species):
    spec_rows = df[df['Species']== species]
    spec_rows.to_csv(species+".csv", sep = ',', index = False)
    
#To test
print(odd_rows(df))
print(spec_count(df))
print(sepal_size(df, 4))
print(spec_file(df, "setosa"))