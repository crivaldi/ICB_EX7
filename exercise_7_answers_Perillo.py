#Answer to Number 1

import numpy as np
import pandas as pd
pwd
cd Desktop/ICB_EX7
pwd

iris=pd.read_csv('iris.csv')

def odd_rows(iris):  
    od_li = [] 
    for index, row in iris.iterrows(): 
        if (index % 2 != 0): 
           od_li.append(row)
    return od_li

print(odd_rows(iris))


#Answer to Number 2

def ret_obs (iris, species):
    obs = (iris['Species'] == species).sum()
    return obs
print (ret_obs(iris, 'setosa'))

def gr8r_than (iris, sepal_width):
    value = iris[iris['Sepal.Width'] > sepal_width]
    return value
print (gr8r_than(iris, 3.5))

def species_file (iris, species):
    row=iris [iris.Species.str.contains(species)]
    row.to_csv(species+'.csv')
species_file (iris, 'virginica')

