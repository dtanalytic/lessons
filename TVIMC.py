import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 18

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

if __name__=='__main__':
    
    
    params = [(5,3),(20,12),(1000,600)]
    
    x = np.linspace(-1,2,1000)
    # uni = stats.uniform(0,1)
    uni = stats.beta(1,2)
    plt.plot(x,uni.pdf(x))
    
    
    fig,ax=plt.subplots(3,1)
    n=5; k=3
    for i,pars in enumerate(params):
        
        apost = stats.beta(1+pars[1],pars[0]-pars[1]+1)
        ax[i].plot(x,apost.pdf(x))
        ax[i].yaxis.set_major_locator(plt.NullLocator())
        ax[i].set_ylabel(f'{pars[0]} подбрасываний')
    ax[2].set_xlabel(f'наблюдаемая вероятность выпадения 0.6 во всех случаях')
    
    # n=1000;k=600
    # apost = stats.beta(1+k,n-k+2)
    # plt.plot(x,apost.pdf(x))
    
    # показываем изменение вероятности в зависимости от увеличения количества подбрасываний
    # n = [5,20,1000]
    # np.random.seed(1)
    # p = 0.62
    # fig, ax = plt.subplots(len(n),3, sharey=True)
    
    # for i,num in enumerate(n):
        
    #     for j in range(3):
    #         x = np.arange(0,num+1)
    #         s_kol = stats.binom(n=num, p=p).rvs()     
            
    #         # ax[i].hist(s_kol/num,label=f'количество испытаний - {num}\nколичество  успехов - {s_kol}', bins=None)
    #         ax[i,j].vlines(s_kol/num,0,0.2,label=f'количество выпадений\nрешки - {s_kol}')
    #         # ax[i,j].vlines(s_kol/num,0,0.2)
    #         # ax[i,j].plot(0, 0, label=f'количество  успехов - {s_kol}', alpha=0)
            
    #         ax[i,j].legend(loc='center left')
            
    #         ax[i,j].yaxis.set_major_locator(plt.NullLocator())
    #         ax[2,j].set_xlabel(f'эксперимент - {j}')
            
    #         # ax[i,j].set_ylabel(f'количество испытаний - {num}')
    #     ax[i,0].set_ylabel(f'всего испытаний - {num}')
    
