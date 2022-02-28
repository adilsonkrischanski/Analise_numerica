# Divided Differences

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [2,5,1,3]

def divided_differences(x,y):
    Y = [item for item in y]
    n = len(y)
    coeffs = [y[0]] + [0] *(n-1)
    for i in range(n-1):
        for j in range(n-1-i):
            numer = Y[j+1]-Y[j]
            denom = x[j+1+i] - x[j]
            Y[j] = numer / denom
        coeffs[i+1] = Y[0]
    
    return coeffs

coeficientes = divided_differences(x,y)

def eq(x,coeficiente):
    n = len(x)
    equation = []
    for i in range(n):
        sign = ''
        if i != 0:
            sign = "*"
        equation += f'{coeficiente[0]:+}{sign}'+'*'.join([f'(x{-xj:+})' for j, xj in enumerate(x) if j < i+1])
    return equation

print(coeficientes)
poly = eq(x,coeficientes)
print(poly)

t= np.linspace(min(x). max(x), 100)

def p(x):
    return eval(poly)

plt.plot(t, p(t))
plt.scatter(x,y, zorder=10)
plt.savefig("diff_div.png")