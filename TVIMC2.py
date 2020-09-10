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
    
    # distr = stats.bernoulli(0.5)
    # x = np.linspace(-1,2,100)
    # plt.vlines(x,0, distr.pmf(x))
    # plt.xlabel('значения случайной величины')
    # plt.ylabel('вероятности значений случайной величины')
    
    x = np.linspace(0,3,1000)
    distr = stats.expon(scale=1./2)
   
    #distr = stats.uniform(loc = 0.3, scale = 0.4)
    # x = np.linspace(0.3,0.7,1000)
    
    plt.plot(x,distr.pdf(x))
    mean, var, skew, kurt = distr.stats(moments='mvsk')
    
    
    
    n_distr = 400
    n_point_new = 1000            
    distr_whole = [[distr.rvs() for _ in range(n_point_new)] for _ in range(n_distr)]
    df = pd.DataFrame(distr_whole)
    means = df.mean(axis=0)
    
    sns.kdeplot(means,label = 'плотность вероятности для средней доли выпадений орла \n при 400 подбрасываниях симметричной монеты')
        
    means.var()
    
    
    
    
    # x = np.linspace(distr.ppf(0.005),
    #             distr.ppf(0.995), 100)
    # plt.plot(x, distr.pdf(x),
    #    'r-', lw=5, alpha=0.6, label='expon pdf')
    
    # distr = stats.norm(0,1)
    # distr.cdf(-1.53)
    
    # (0.5375 - 0.5)/np.sqrt(0.0006)
    
    # x = np.linspace(-0.5,1.5,1000)
    # norm = stats.norm(0.5,0.2)
    # plt.plot(x,norm.pdf(x))
    
    # n_distr = 100
    # n_point_new = 1000
    # distr = stats.norm(0.5,0.2)
    
    
    # distr_whole = [[distr.rvs() for _ in range(n_point_new)] for _ in range(n_distr)]
    
    # df = pd.DataFrame(distr_whole)
    # means = df.mean(axis=0)
    
    # sns.kdeplot(means)
