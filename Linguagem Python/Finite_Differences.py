# Finite Differences
import random
import numpy as np

def f(x):
    return x**x

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n  = len(xs)

    for i in range(n):
        # Para contruir a matriz A
        A.append([0] *n)
        for j in range(n):
            A[i][j] = xs[j] ** i
        
        # Para contruir a matriz B
        potencias = [k+1 for k in range(i - ordem, i)]
        fatorial = 0 if i< ordem else prod(potencias)
        termo = fatorial * x0 ** (i-ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A, B)
    # Contruir a soma que da a aproximacao
    soma  = 0
    for ck,xk in zip(cs,xs):
        soma += ck*f(xk)

    return soma

if __name__ == '__main__':

    x0 = 2
    ordem = 1
    
    # Pontos para contruir a formula
    num_pontos = 2
    a = x0 - 0.25
    b = x0 + 0.25
    xs = [a+(b-a) * random.random() for _ in range(num_pontos)]
    xs.sort() # Lista de coordenadas x

    r = finite_diffs(xs, ordem, x0, f)

    print(f'Aproximação para a derivada de {ordem} de f no ponto {x0}: ', r)