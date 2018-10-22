#Loading iris.csv
import pandas as pd
irisdata=pd.read_csv('iris.csv')
#1 Write a function that returns the odd rows of irisdata
def odd(x):
    odd_rows=[x.iloc[1::2]]
    return odd_rows
answer=odd(irisdata)
print answer

#2.1 Number of observations for a given species 
def species(y):
    Number=irisdata[irisdata.Species.str.contains(y)]
    return Number
virginica=species('virginica')
setosa=species('setosa')
versicolor=species('versicolor')
def count(x):
    count=x['Species'].value_counts()
    return count
final_answer_virginica=count(virginica)
print final_answer_virginica
final_answer_setosa=count(setosa)
print final_answer_setosa
final_answer_versicolor=count(versicolor)
print final_answer_versicolor

#2.2 Return a dataframe for flowers with Sepal.Width greater than a specified value
def width(x):
    rows=irisdata[irisdata['Sepal.Width']>x]
    return rows
print width(2)
print width(4)
print width(4).shape
print width(3.6)

#2.3 Write the data for a given species to a comma-delimited file
def species_1(x):
    species_1=irisdata[irisdata.Species.str.contains(x)]
    str1=x
    str2=".csv"
    file=str1+str2
    species_1.to_csv(file)
    Species=pd.read_csv(file)
    return Species
print species_1('setosa')
print species_1('versicolor')
print species_1('virginica')
