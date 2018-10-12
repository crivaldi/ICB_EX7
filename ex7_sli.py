# This script is for Exercise 7 by Shuyue Li

# Q1

import pandas as pd

def odd(df):
    ''' 
    This function is aimed to return the add rows of a pandas dataframe
    df should be a pandas dataframe
    '''
    nrow = df.shape[0]
    odds = pd.DataFrame()
    for i in range(1,nrow):
        if i%2 == 0:
            continue
        else:
            odds = odds.append(df.iloc[i,:])
    return odds

# test data
iris = pd.read_csv("iris.csv", delimiter = ",")
print odd(iris)
    

# Q2

def ct_sp(data,species):
    '''
    This function is aimed to return the number of observations for a given 
        species included in the data set
    data should be a pandas dataframe; species should be a string
    '''
    sp = data.loc[data['Species']==species]
    return sp.shape[0]

# test data
iris = pd.read_csv("iris.csv", delimiter = ",")
print ct_sp(iris,"setosa")  


def select_sepal(data,width):
    '''
    This function is used to return a dataframe for flowers with Sepal.Width 
        greater than a value specified by the function user
    data is a pandas dataframe; width is specified width
    '''
    if width > data["Sepal.Width"].max():
        print "Invalid value: larger than maximum width"
    else:
        select = data.loc[data['Sepal.Width'] > width]
    return select

# test data
iris = pd.read_csv("iris.csv", delimiter = ",")
print select_sepal(iris,3.5) 


def extract_species(data,species):
    '''
    This function is used to select a given species and save to a csv file
    data should be a pandas dataframe; species should be a string
    '''
    sp = data.loc[data['Species']==species]
    file_name = str(species) + ".csv"
    sp.to_csv(file_name, sep=',')

# test data
iris = pd.read_csv("iris.csv", delimiter = ",")
extract_species(iris,"setosa") 