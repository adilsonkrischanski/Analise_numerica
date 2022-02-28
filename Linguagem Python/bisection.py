import math
def f(x):
    M_PI = 3.141592
    return 1000*(((4/3) * (M_PI*8.28*8.28*8.28))-( ((M_PI*x*x)/3) * (3*8.28-x))) - 241.72*(4/3) * (M_PI*8.28*8.28*8.28) #funcao

def bisection(f,a,b,n):
    if f(a)*f(b)>=0:
        print(f'o metodo de bolzano nao sabe dizer se existe')
        return
    else:
        for i in range(0,n):
            m = 0.5*(a+b)
            print(f'x_{i+1} = {m:.16f}')
            if f(m)==0:
                print(f'voce achou uma raiz exata para f:z = {m:.16f}')
            if(f(a)*f(m)<0):
                b=m
            else:
                a=m

def main():
    a=0.0
    b=16.5
    n=12
    bisection(f,a,b,n)

main()
