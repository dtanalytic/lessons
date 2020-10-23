import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


if __name__=='__main__':
    
    train = pd.read_csv('../data/electro/train.csv')
    test = pd.read_csv('../data/electro/test.csv')
    
    train.columns
    vis_vars = ['temperature', 'var1', 'pressure', 'windspeed', 'var2']
    
    fig, axes = plt.subplots(len(vis_vars),1)
    for ax, vis_var in zip(axes.flatten(),vis_vars):
        train.plot(kind='scatter', ax=ax ,x=vis_var,y='electricity_consumption')
    
    
    train.plot(kind='scatter',x='temperature',y='electricity_consumption') 
    


    
    # добавляем признаки времени
    # def get_feat1(date_str,fmt):
    #     date = datetime.strptime(date_str,fmt)
    #     return date.month
    # fmt =  '%Y-%m-%d %H:%M:%S'   
    # date_col1 = train['datetime'].map(lambda x: get_feat1(x,fmt))
    # date_col1 = pd.get_dummies(date_col1)   
    
    
    # def get_feat2(date_str,fmt):
    #     date = datetime.strptime(date_str,fmt)
    #     return date.timestamp()
    # fmt =  '%Y-%m-%d %H:%M:%S'   
    # date_col2 = train['datetime'].map(lambda x: get_feat2(x,fmt))
    
    
    # data_tr = train.copy()
    # data_tr = pd.merge(data_tr,date_col1,left_index=True, right_index=True)
    # data_tr['sec'] = date_col2
    
    # data_tr.dropna()
    
    # data = data.set_index(date_col)
    # data.resample('M')
    
    
    # #  средства pandas извлечение признаков времени
    # date_col = pd.to_datetime(train['datetime'].values)
    # date_col.map(lambda x: x.value)
    # date_col2 = date_col.astype(np.int32)
    # date_col3 = pd.to_datetime(date_col2) 
    # # средства datetime извлечения признаков времени
    # train['datetime'].map(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
    # train.loc[0,'datetime']
    # sec = datetime.strptime(train.loc[0,'datetime'],'%Y-%m-%d %H:%M:%S').timestamp()
    # sec/(24*60*60*365)