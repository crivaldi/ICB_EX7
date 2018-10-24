#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:31:15 2018

@author: saurylara
"""


#Import the wages file
import pandas 
wages = pandas.read_csv("/Users/saurylara/Desktop/wages.csv")

#Create function that returns odd rows of any pandas dataframe
def odder (filename):
    headfile = filename[1: :2]
    return headfile

print(odder(wages))

#Import the iris file
iris = pandas.read_csv("/Users/saurylara/Desktop/IBC_EX6/iris.csv")

#Create function that returns the number of observations of a species for given dataset
def observer (filename,speciesname):
    numobservations= filename[filename['Species']==speciesname].count()['Species']
    return numobservations

print(observer(iris,"setosa"))

#Create function that returns a dataframe for flowers with Sepal.Width greater than specified value
def dataframe (filename, widthvalue):
    numSepalWidth = iris[iris['Sepal.Width'] > widthvalue]
    return numSepalWidth

print(dataframe(iris,3.0))

#Create function that writes data for given species to comma-deliminated file with given species name as the file name
def dataredirector (filename, speciesname):
    dataSpecies = iris[iris['Species']==speciesname]
    dataSpecies.to_csv(speciesname+'.csv')
    return 0

dataredirector(iris,"virginica")

