from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 18

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

if __name__=='__main__':

    np.random.seed(1)
    # последовательность 100 равноудаленных точек
    # на отрезке от -2 до 2
    x = np.linspace(-2,2,100)
    # линейна связь с добавлением небольшого шума,
    # имеющего стандартное нормальное распределение
    y = 2*x - 1 + np.random.normal(0,1,100)
    plt.scatter(x,y)
    plt.title('Диаграмма рассеяния X и Y')
    plt.xlabel('X')
    plt.ylabel('Y')


    y=x**2
    plt.scatter(x,y)
    plt.title('Диаграмма рассеяния X и Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    
    

    x = [0]*30+[1]*70 
    y = [0]*15 +[1]*15+[0]*7+[1]*63
    pearsonr(x,y)
