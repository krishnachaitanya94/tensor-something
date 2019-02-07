# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:05:13 2019

@author: kcgov
"""

import pandas as pd 
import numpy as np
import json

Food_Composition=pd.read_csv("Food Composition.csv")

Food_Words = Food_Composition.iloc[3:,0:2]

Rows=Food_Words.shape[0]
j=0
p=0

Food_Dict={}
Food_List = []
for i in range(Rows-1):
    Department = Food_Words.iloc[i,0]
    Word= Food_Words.iloc[i,1]
    
    
    if not (pd.isnull(Department)):
        Food_List = ()
        key = Department
        Food_Dict[key]=Food_List

        Food_List.add(Word)

    else:
        Food_List.add(Word)

with open('Word_Dict.txt', 'w') as file:
     file.write(json.dumps(Food_Dict))
        
        
    