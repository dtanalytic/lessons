import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 18

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

if __name__=='__main__':
    
    # df = pd.read_csv('../data/income.csv')
    # df.plot()
    # plt.plot(df.index, df.income)
    # df['income'].plot()
    # sns.lineplot(data=df)
    # df.plot(kind='line')
    # sns.lineplot(x=df.index, y=df.income)
    # df.income.plot()

    # df = pd.read_csv('../data/dataset_209770_6.txt', sep =' ') 
    # df.plot(kind='scatter', x='x',y='y')
    # plt.scatter(df['x'], df['y'])
    # sns.scatterplot(df.iloc[:, 0], df.iloc[:, 1])
    
    # df = pd.read_csv('../data/genome_matrix.csv') 
    # df=df.drop('Unnamed: 0',axis=1)
    # sns.heatmap(data=df, cmap='viridis')
    # plt.matshow(df, cmap='viridis')
    
    # df = pd.read_csv('../data/dota_hero_stats.csv')
    # num = df['roles'].map(lambda x: len(eval(x)))
    # num.value_counts().plot(kind='bar')

    df = pd.read_csv('../data/iris.csv')
    df = df.drop(['Unnamed: 0'],axis=1)
    
    # df.plot(kind='kde', subplots=True)
    # df.plot(kind='hist', subplots=True)
    
    # for column in df.columns:
    #      sns.distplot(df[column])
    
    # sns.violinplot(df['petal width'], orient ='v')
    
    sns.pairplot(df, hue = 'species')
    
    
    
    
