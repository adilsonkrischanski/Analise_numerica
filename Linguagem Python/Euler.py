import matplotlib.pyplot as plt
import numpy as np


def euler(f,x0:float, y0 :float, h:float, n:int):
    xs, ys = [],[] # lista de pontos interados

    for k in range(n):
        x = x0 + k * h
        y = y0 + h * f(x,y0)
        # uma aprocimação para phi(xk)
        y = y0 + h * f(x0 + k * h, y0)
        print(f'x_{k+1} = {x0 + (k+1)*h}\ny_{k+1} = {y}\n') #print result
    #     xs.append(x+h)
    #     ys.append(y)
        y0 = y
    # return xs,ys



#exemplo 
x0 = 0.48445
y0 = 0.77146
def f(x,y): 
    #return x+y 
    return y*(1-x)+x+2
    pass

r = euler(f, x0, y0, h=0.14143, n=10)
# i=0
# for x,y in zip(*r):
#     k=1
#     i+=1
#     print(f'x_{i} = {x0 +(k)}\ny_{i}={y}\n')


# xs, ys =r
# plt.scatter(xs,ys)
# plt.savefig('euler.png')