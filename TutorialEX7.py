# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:12:41 2018

@author: Alicia
"""
import pandas as pd

data = pd.read_csv("iris.csv")

def odd_rows(fname):
    n = fname.shape[0]
    r = range(0, n, 2)
    cut_section = fname.iloc[r]
    return cut_section
print (odd_rows(data))

def num_species_obs(data):
    count=data.groupby(["Species"], sort=False).size()
    return count
print (num_species_obs(data))
    
def SepalWidth(x, data):
    sorted_data=data.sort_values('Sepal.Width')
    part3 = (sorted_data.loc[sorted_data['Sepal.Width'] > x])
    return part3
#print (SepalWidth(user value, data))

def species_to_csv(data):
    sorted_data=data.sort_values('Sepal.Width')
    part4 = (sorted_data.loc[sorted_data['Species'] == 'setosa'])
    return part4.to_csv("setosa.csv")
