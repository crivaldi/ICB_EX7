# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:48:30 2018

@author: vysan
"""

import pandas as pd
def oddrows(filename):
    data=pd.read_csv(filename,header=0,sep=",")
    return data.iloc[1::2]
print oddrows("filename") #filename is the name of the file with your dataframe 





