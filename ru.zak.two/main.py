import numpy as np
import random
a = [[3, -2],
    [5, 4]]
#b = np.matrix(np.random.randint(100, size=(2, 1)))
b = [[6],
    [32]]


def Cramer(a, b):
    determ = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    determx = b[0][0]*a[1][1] - b[1][0]*a[0][1]
    determy = b[1][0]*a[0][0] - b[0][0]*a[1][0]
    x = determx//determ
    y = determy//determ
    return print(x, y)

def Gauss(a,b):
    a[0][0] /= 3
    a[1][0] //= 3
    b[0][0] /= 3
    a[0][1] = (a[0][1]-a[0][0]*a[0][1])/(22/3)
    a[1][1] = (a[1][1] - a[1][0] * 5)/(22/3)
    b[1][0] = (b[1][0]-b[0][0]*5)/(22/3)
    a[0][0] = a[0][0]+a[0][1]*(2/3)
    a[1][0] = a[1][0]+a[1][1]*(2/3)
    b[0][0] = b[0][0]+b[1][0]*(2/3)

    return print(b)
Cramer(a, b)
Gauss(a, b)
