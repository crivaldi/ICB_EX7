# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 19:42:38 2018

Exercise 7: Patricia Portmann

@author: Patricia
"""
import pandas

# function that takes in the full dataframe argument
# and returns only the odd numbered rows stored in a dataframe
def OddRows(dataframe):
    OddDF = dataframe.iloc[1::2] # only puts odd numbered rows into OddDF dataframe
    return OddDF # function returns odd rows

# function that takes in dataframe and species name argument
# and returns the count for the specific species
def NumObs(dataframe,species):
    count=0 # count initialized to 0
    totalrows=dataframe.shape[0] # finds length of df
    for x in range(totalrows):
        # conditional that matches the 4th column to specified species
        if dataframe.iloc[x,4] == species:
            count += 1
    return count

# function that takes in dataframe and specified width limit
# and returns a dataframe only with the row that are greater than the width limit
def SepWidth(df, width_limit):
    return(df.loc[df['Sepal.Width']>width_limit]) 
    
# function that takes in dataframe and specified species
# and makes a .csv file for the species with format "speciesname.csv"
def toCSV(df,species):
    specific_df=df.loc[df['Species']==species]
    filename = "%s.csv" %species
    specific_df.to_csv(filename,header=True,index=False,sep=",")  


# main body code
data=pandas.read_csv("iris.csv") # data loaded into a data frame

# calls for function OddRows
OddDF = OddRows(data)
# print(OddDF)

# calls for function NumObs
species = raw_input("What species are you counting? ")
number_observations = 0
if species == "setosa"  or species == "versicolor" or species == "virginica":
    number_observations = NumObs(data,species)
    print(species, "has: ", number_observations, "observations")
else: 
    print("invalid species name")


# ask for user input
limit = float(input("Type sepal width: ")) # save user input as float variable limit
# calls for function to return a dataframe w/ Sepal.Width greater than limit 
Sepal_Width_df = SepWidth(data,limit)
print(Sepal_Width_df)


sp_csv = raw_input("What species are you making a .csv file for? ")
if species == "setosa"  or species == "versicolor" or species == "virginica":
    toCSV(data,sp_csv)
    print(".csv file for:", sp_csv, "made.")
else: 
    print("invalid species name.")