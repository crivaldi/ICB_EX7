# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:11:34 2018

@author: Rachel R
"""
# Question 1
import pandas as pd
irisdata = pd.read_csv("/Users/Rachel R/Desktop/data-shell/IBC_EX6/iris.csv")

def cut_sect(file):
    cut_section = file.iloc[::2]
    return cut_section

print cut_sect(irisdata)

# Question 2
#Return the number of observations for a given species included in the data set
def species_cut():
    observations = irisdata["Species"].value_counts()
    return observations
print species_cut()

#Return a dataframe for flowers with Sepal.Width greater than a given value specified by the function user
def sepalwidth_cut(x):
    Sepalwidth = irisdata.loc[irisdata["Sepal.Width"] > x]
    return Sepalwidth
print sepalwidth_cut(3)

#Write the data for a given species to a comma-demilited file with the given species name as the file name: Hint: look at + or % to concatenate your species name and ".csv"
def species_cut(x):
    x = irisdata[irisdata["Species"]=="virginica"]
    x.to_csv("virginica")
    return x
print species_cut("virginica")
