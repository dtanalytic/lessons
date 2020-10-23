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
    
    
    # loc, scale  = 0,1    
    # distr = stats.norm(loc=loc, scale = scale)
    # distr.ppf(0.975)    
    # distr.ppf(0.95)
    # mean, var= distr.stats(moments='mv')
    
    # points_num=10000
    # distr.rvs(size=points_num) 
    # sns.kdeplot(distr.rvs(size=points_num), label = f'Нормальное распределение со средним {loc}\nи стандартным отклонением {scale},\nполученное путем случайной выборки {points_num} точек')
        
    # # x = np.linspace(-4,4,1000)
    # # plt.plot(x,distr.pdf(x), label  = f'Нормальное распределение со средним {loc}\nи стандартным отклонением {scale}')
    # # plt.legend()
    
    
    
    # x = np.linspace(0,3,10000)    
    # lambda_ = 4
    # distr = stats.expon(scale=1/lambda_)
    # distr.pdf(x)    
    # plt.plot(x,distr.pdf(x), label= f'Распределение экспоненциальной случайной\nвеличины с параметром lambda_ равным {lambda_}')
    # plt.legend()
    
    
    
    # distr.rvs((2,5))
    # distr.cdf(-1)
    # distr.pmf([0,0,0,1])
    # pdf
    # distr.ppf(0.99)
    # mean, var, skew, kurt = distr.stats(moments='mvsk')
    
    
    
    
    mu=3
    distr = stats.poisson(mu=mu)    
    points_num=10
    x = np.arange(10)
    plt.vlines(x,0,distr.pmf(x),label = f'Пуассоновское распределение вероятности {points_num} неотрицательных\nцелых значений с параметром mu = {mu}')
    plt.legend()
    

    
    # distr.pmf([0,0,0,1])
    
    # beg = 0
    # width = 1
    # distr = stats.uniform(loc = beg, scale = width)
    # points_num=10000
    # x = distr.rvs(size=points_num)  
    # distr.cdf(x)      
    
    # sns.lineplot(x,distr.cdf(x), label = f'Кумулятивная функция распределения\
    #              \nдля равномерного распределения на отрезке [{beg},{beg+width}]')
    # plt.xlim(-0.5,1.5)     
    
    # x = np.linspace(-1,2,100) 
    # plt.plot(x,distr.pdf(x), label = f'Равномерное распределение\nна отрезке [{beg},{beg+width}]')
    # plt.legend(loc='upper right')
    
       

    
    # # bernoulli
    # x = np.linspace(-1,2,10)
    # p = 0.4
    # distr = stats.bernoulli(p=p)
    # plt.vlines(x,0,distr.pmf(x), label = f'Распределение Бернулли с параметром p={p}')
    # plt.legend()
     

    # n=50;p=0.3
    # x = np.arange(51)
    # distr = stats.binom(n=n,p=p)
    # plt.vlines(x,0, distr.pmf(x),label = f'Распределение вероятности количества успехов \nв схеме длины {n} с вероятностью успеха {p}')
    # plt.legend()
    # plt.xlim([0,35])
    
    # x = np.arange(12)
    # mu=3
    # distr = stats.poisson(mu=mu)
    # plt.vlines(x,0,distr.pmf(x),label = f'Пуассоновское распределение вероятности неотрицательных\nцелых значений с параметром mu = {mu}')
    # plt.legend()
    
    # low = 2; high = 8
    # distr = stats.randint(low = low, high = high)
    # x = np.arange(low-1,high+2)
    # plt.vlines(x, 0, distr.pmf(x), label = f'Равномерное дискретное\nрапределение на\nполуинтервале [{low},{high})')
    # plt.legend(loc='best')
    
    # beg = 0.3
    # width = 0.4
    # distr = stats.uniform(loc = beg, scale = width)
    # x = np.linspace(0,1,100)    
    # plt.plot(x,distr.pdf(x), label = f'Равномерное распределение\nна отрезке [{beg},{beg+width}]')
    # plt.legend(loc='upper right')
    
    # loc, scale  = 0.5,0.2
    # x = np.linspace(-0.5,1.5,1000)
    # distr = stats.norm(loc=loc, scale = scale)
    # plt.plot(x,distr.pdf(x), label  = f'Нормальное распределение со средним {loc}\nи стандартным отклонением {scale}')
    # plt.legend()
    
    
    # x = np.linspace(0,3,1000)
    # lambda_ = 4
    # distr = stats.expon(scale=1/lambda_)
    # plt.plot(x,distr.pdf(x), label= f'Распределение экспоненциальной случайной\nвеличины с параметром lambda равным {lambda_}')
    # plt.legend()
    # mean, var, skew, kurt = distr.stats(moments='mvsk')
        


    
    