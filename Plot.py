import matplotlib.pyplot as plt
import numpy as np

#Main function
def plot(L,c="inferno"):
    x=[i[0] for i in L]
    y=[i[1] for i in L]
    z=np.arange(0,len(L))
    plt.scatter(x,y,c=z,cmap=c)
    plt.show()

#Test
'''
L={(0.0, 1), (-1, 0.5), (0, 0.5), (2.0, 2), (1, 1.0), (1.0, -1), (-0.5, 0)}
plot(L)
'''
