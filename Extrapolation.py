from matplotlib import pyplot as plt
import numpy as np
from math import *

def clean(L):
    x = [i[0] for i in L]  # extracts X-points from L
    y = [i[1] for i in L]  # extracts Y-points from L
    i = 0
    while i < (len(L) - 1):  # Removes the discontinuous points from the arranged list of points
        if abs(x[i + 1] - x[i]) > 1 and abs(y[i + 1] - y[i]) > 1:
            L.pop(i + 1)
            x.pop(i + 1)
            y.pop(i + 1)
            i -= 1
        i += 1
    return L

def extrapolate(L,n=1):
    '''
    Reads the points and give data points and parameters for the wave functions
    :param L: List of points arranged
    :param n: Number of times the wave shall be repeated for curve fitting
    :return: X-data and Y-data with time T and HCF of angular wave numbers
    '''
    x=[i[0] for i in L] #extracts X-points from L
    y=[i[1] for i in L] #extracts Y-points from L
    t=np.arange(0,n*len(L)) #Creates list of time
    X,Y=[],[]
    for i in range(n): #Repeats the data-points n times
        X.extend(x)
        Y.extend(y)
    return X,Y,t,2*pi/len(L) #Angular Wave Number

def plot(L,n):
    x,y,t,k=extrapolate(L,n)
    plt.plot(t,x)
    plt.plot(t,y)
    plt.show()

#Test
#L=[(0.0, 1), (0, 0.5), (-0.5, 0), (-1, 0.5), (1, 1.0), (2.0, 2), (1.0, -1)]