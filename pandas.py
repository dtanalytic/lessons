
import numpy as np
from scipy import sparse
from os import path
import random
import pandas as pd


if __name__ == '__main__':
    
   stud = pd.read_csv('../data/students.csv')


   stud[(stud['reading score'] > 50) & (stud.gender == 'female')]

   stud_part = stud[stud.lunch=='free/reduced']
   len(stud_part)/len(stud)
   
   stud_part.mean()
   stud_part.var()
   
   m_v  = stud[['math score', 'reading score','writing score']]\
       .groupby(stud.lunch)\
       .aggregate(['mean','var'])
   
   stud.loc[stud.lunch=='free/reduced',['math score', 'reading score','writing score']].mean()
   
   
   # degrs = ["bachelor's degree", "master's degree"]
   # degr_col = 'parental level of education'
   # stud.query('@degr_col == @degrs[0]')
