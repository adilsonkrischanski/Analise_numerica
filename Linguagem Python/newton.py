import math

def f(x):
    e = 2
    return x*x - 4*x - math.log(e,x) +2 # function

def df(x):
    return 2*x -1/x -4 # derivada de f

def newton(x0,n):
    for i in range(0,n):
        x1 = x0-(f(x0)/df(x0))
        print(f'x_{i+1} = {x1:.7f}')
        x0=x1

def main():
    x0=3.1074
    n=5
    newton(x0,n)

main()

