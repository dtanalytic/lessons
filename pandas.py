
import numpy as np
from scipy import sparse
from os import path
import random
import pandas as pd


if __name__ == '__main__':
    
   stud = pd.read_csv('../data/students.csv')

   stud_part = stud[stud.lunch=='free/reduced']
   len(stud_part)/len(stud)
   
   m_v  = stud[['math score', 'reading score','writing score']]\
       .groupby(stud.lunch)\
       .aggregate(['mean','var'])
   
