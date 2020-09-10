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
    
        
    
    n = [5,10,20,50,70,100,200,300,500, 700, 1000]
    N=200
    p=0.5
    distr = stats.bernoulli(p)
    Zm_vars = []
    Zm_l=[]
    for num in n:
        Z = distr.rvs(size=(num,N))
        Zm = Z.mean(axis=0)
        Zm_l.append(Zm[0])
        Zm_vars.append(((Zm - p)**2).mean())
        
    plt.plot(n,Zm_vars, alpha=0.6, color='brown', label = 'дисперсия средних')
    plt.plot(n,p*(1-p)/np.array(n), linestyle='dotted',color='black', label = 'p*(1-p)/n')
    plt.legend()
    
    plt.plot(n, Zm_l, label = 'Доля выпадений орла в зависимости от количества подбрасываний')
    plt.legend()

    




