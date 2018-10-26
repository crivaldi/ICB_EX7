#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:53:06 2018

@author: ColinSheehan
"""

def oddfunction(filename): #remember to put filename in quotes #assumes you already imported numpy and pandas as pd
    data = pd.read_csv(filename)
    length = len(data)
    for num in range(0, length):
        line = data.iloc[num, :]
        constant=num % 2
        if constant==0:
            print(line) #we actually want even because how python counts, assuming first row is actually 1 not 0
        else:
            print("...................................")
        #I ran the function as >oddfunction("wages2.csv")
        