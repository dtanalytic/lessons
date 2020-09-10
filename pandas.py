
import numpy as np
from scipy import sparse
from os import path
import random
import pandas as pd


if __name__ == '__main__':
   
   df = pd.DataFrame({'name':['A','B','A','D'], 'value':[1,2,4,10]}, index=['row1','row2','row3','row4'])
   df = pd.DataFrame([['A',1],['B',2],['C',4],['D',10]], index=['row1','row2','row3','row4'], columns=['name', 'value'])
   df.loc[(df.value>2) & (df.name=='A') ]
  
   
   df = pd.DataFrame({'salary $':[1000,2000,4000,3000]}, index=['Alice.Dep1','Jill.Dep2','Bob.Dep1','Chris.Dep3'])
   
   df.filter(like='Dep1',axis=0)
   
   
   my_stat = pd.read_csv('../data/my_stat1.csv')
   
   subset_1 = my_stat.iloc[:15,[0,1]]
   subset_2 = my_stat.drop([0,1],axis=0).iloc[:,[2,3]]
   
   subset_1 = my_stat.loc[(my_stat.V1>0) & (my_stat.V3=='A') ]
   subset_2 = my_stat.loc[(my_stat.V2!=10) | (my_stat.V4>=1) ]
   
   subset_11 = my_stat.query('V1>0 & V3=="A"')
   
   my_stat = my_stat.assign(V5=my_stat.V1+my_stat.V4,V6=np.log(my_stat.V2))
   
   my_stat.columns  = ['session_value', 'group', 'time', 'n_users'] 
   
   my_stat.rename(inplace=True,columns={"V1": "session_value", "V2": "group", 'V3':'time','V4':'n_users'})
   my_stat.rename(inplace=True,index={0: "row1"})
   
   my_stat[my_stat['session_value'].isnull()]
   my_stat['session_value'].fillna(0, inplace=True)
   
   
   my_stat.loc[my_stat.n_users>=0,['n_users']].median()
   
   my_stat.loc[my_stat.n_users<0,['n_users']] = int(my_stat.loc[my_stat.n_users>=0,['n_users']].median())
   
   
   mean_session_value_data = my_stat.groupby('group', as_index=False).aggregate({'session_value':'mean'}).rename(columns={'session_value':'mean_session_value'})
   
   # df = pd.read_csv('../data/dota_hero_stats.csv')
    
   # legs_grs = df.groupby('legs')['localized_name'].nunique()
   # df.groupby('legs')['localized_name'].count()
   
   # df.groupby(['attack_type','primary_attr'])['roles'].count()
   
   
   
   
   # df = pd.read_csv('../data/accountancy.csv')
   
   # df.groupby(['Executor', 'Type'], as_index=False).mean()
   
   
   
   # concentrations = pd.read_csv('../data/algae.csv')
   # concentrations.groupby(['genus'])[['sucrose', 'alanin', 'citrate', 'glucose', 'oleic_acid']].mean()


   # alanin = concentrations.groupby(['genus']).aggregate(['mean','min', 'max']).loc['Fucus','alanin']
   
   # concentrations.groupby(['genus']).aggregate(['mean','min', 'max']).loc['Fucus','alanin']
   
   # concentrations.groupby('group')['sucrose'].apply(lambda g:g.max() - g.min())
   # concentrations.groupby('group')['species'].count()
   # concentrations.groupby('group')['citrate'].var()
   
   # df = pd.read_csv('../data/column_hell.csv')
   
   # selected_columns = df.filter(like='-')
   
   
   # stud = pd.read_csv('../data/students.csv')


   # stud[(stud['reading score'] > 50) & (stud.gender == 'female')]

   # stud_part = stud[stud.lunch=='free/reduced']
   # len(stud_part)/len(stud)
   
   # stud_part.mean()
   # stud_part.var()
   
   # m_v  = stud[['math score', 'reading score','writing score']]\
   #     .groupby(stud.lunch)\
   #     .aggregate(['mean','var'])
   
   # stud.loc[stud.lunch=='free/reduced',['math score', 'reading score','writing score']].mean()
   
   
   # degrs = ["bachelor's degree", "master's degree"]
   # degr_col = 'parental level of education'
   # stud.query('@degr_col == @degrs[0]')
