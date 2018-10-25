# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:15:49 2018

@author: vysan
"""
#return number of observations for given species
import pandas as pd
data=pd.read_csv("iris.csv",header=0,sep=",")
def count(name): 
    return (data["Species"]==name).sum()
count("name") #name is the name of the species of interest



#return dataframe for flowers with Sepal.Width > than specified value 
import pandas as pd
data=pd.read_csv("iris.csv",header=0,sep=",")
def sepalwidthgreaterthan(x):
    return data[data["Sepal.Width"] > x]
sepalwidthgreaterthan(x) #x is the specified value by the user 



#write data for given species to comma-delimited file
#with name "speciesname".csv
import pandas as pd
data=pd.read_csv("iris.csv",header=0,sep=",")
def newfilefor(name):
    new=data[data["Species"]==name]
    new.to_csv(str(name)+".csv",sep=(","))
newfilefor("name") #name is the name of the given species



