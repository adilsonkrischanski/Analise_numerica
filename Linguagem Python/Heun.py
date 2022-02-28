# Metodo de Heun

def heun(f, x0, y0, h, n):
    r = []
    for _ in range(10):
        m1 = f(x0,y0)
        m2 = f(x0+h, y0+h *m1)
        y1 = y0 + h *(m1+m2)/2

        #atualizando os valores
        x0 += h
        y0 = y1
        r.append((x0,y0))
    return r


#exemplo 
def f(x, y):
    #return 1+x*y
    return y*(2-x)+x+1

if __name__ == '__main__':

    
    x0 = 0.27678
    y0 = 1.18853 
    h = 0.14336

    r = heun(f, x0, y0, h, n=10)
    
    for i,x in enumerate(r,1):
        xi,yi=x
        print(f'x_{i} = {xi}\ny_{i} = {yi}\n')

 