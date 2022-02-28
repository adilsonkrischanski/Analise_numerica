#metodo do ponto medio de Euler

import re
import numpy as np
import matplotlib.pyplot as plt


# pvi y'= x+y, y(0)= 1
# sol y(x) = 2*esp(x) -x -1



def eulermp(f, x0, y0, h,n):
    for k in range(n):
        m1 = f(x0,y0)
        m2 = f(x0+h /2, y0+h*m1/2)
        y1 = y0 + h *m2
        #atualizando 
        x0 += h
        y0 = y1
        yield x0,y0
        


def f (x,y):
    #return x+y
    return y*(2-x)+x+1

if __name__ =='__main__':
    x0 = 0.99769
    y0 = 1.32272
    h = 0.12729
    n =10
    resp = list(eulermp(f,x0,y0,h,n))

    for i,x in enumerate(resp,1):
        xi,yi=x
        print(f'x_{i} = {xi}\ny_{i} = {yi}\n')


    # professor disse q podemos ignorar

    def y(x):
        return 2*np.exp(x) -x -1
        

    t = np.linspace(x0,x0+n * h,120) #120 set quantidade de espaço
    yt = [y(ti) for ti in t] #depende de funcao

    # plt.plot(t,yt)
    # xs,ys = zip(*resp)
    
    # plt.scatter(xs,ys)

    # plt.savefig("eulermp.png")


     