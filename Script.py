# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:55:47 2018

@author: Annaliese
"""
# import functions
import numpy as np
import pandas as pd

# import data
data = pd.read_csv('iris.csv')

# write a function that returns the odd rows of any pandas dataframe 

def odd_row_selector(dataframe):
    nrows = dataframe.shape[0]
    rows = range(0, nrows)
    array_rows = np.asarray(rows)
    odd_rows = array_rows[array_rows % 2 != 0]
    return dataframe.iloc[odd_rows, ]

odd_row_selector(data)

###################################################################

# return number of observations for a species
data.Species.value_counts()['setosa']

def ob_count(species):
    '''Returns the number of obsevations for a species name inputted as 
    a character string'''
    return data.Species.value_counts()[species]

# example
ob_count("setosa")

# obtain a data frame for flowers with sepal width larger than user inputted 
# value
def bigger_sepal_width(n):
    return data[data["Sepal.Width"] > n]
    
# example
bigger_sepal_width(4)

# write data for a given species to a csv file with the species name as file 
# name

def species_to_csv(species):
    '''input species as string'''
    small_data = data[data["Species"] == species]
    small_data.to_csv(species + ".csv")
    
# example   
species_to_csv("virginica")
    


