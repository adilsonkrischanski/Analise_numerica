def lagrange(x,y):
    # a eq do polinomio de lagrange
    n = len(x)
    if n == len(y):
        eq=''
        for k in range(n):
            numer = '*'.join([f'(x-{xi:+})' for  i,xi in enumerate(x) if i !=k ])
            denom = '*'.join([f'({x[k]}{-xi:+})'for  i,xi in enumerate(x) if i !=k ])
            eq += f'{y[k]:+}*({numer})/({denom})'
        return eq
    else:
        raise TypeError('O numero de coordenadas x é diferentes do numero de coordenadas em y')


if __name__ == '__main__':

    x = [1,2,3] # coordenadas x do ponto
    y = [2,5,1] # coordenadas y do ponto

    eq = lagrange(x,y)

    def subs(x):
        return eval(eq)
    
   


    #fenomeno de Runge

    def f(x):
        return 1 / (1 + 25 * x ** 2)

    num =5 #quantidade de pontos

    x2 = [-1 + (2/(num-1)) * i for i in range(num)]
    y2 = [f(i) for i in x2]

    eq2 = lagrange(x2,y2)

    #subs

    def subs(x):
        return eval(eq2)
        
    print('p(x) =',eq2)
    print(subs(1))

    print(x2)
    print(y2)


    # vamos plotar os graficos

    from matplotlib import pyplot as  plt  # pip3 install matplotlib 
    import numpy as np

    t= np.linspace(-1,1,200)

    plt.plot(t,subs(t),label='lagrange')
    plt.plot(t,f(t),label='funcao')
    plt.scatter(x2,y2)
    plt.legend()

    plt.savefig('lagrange.png')
    
