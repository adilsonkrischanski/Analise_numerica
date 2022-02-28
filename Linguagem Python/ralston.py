# Metodo  de Ralston

def ralston(f, x0, y0, h, n):
    r =[]
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0+(3/4)*h, y0+(3/4)*h*m1)
        yk = y0 + h *(m1 + 2*m2)/3
        # at valores

        x0  += h
        y0 = yk
        r.append((x0,y0))
    
    return r




if __name__ == '__main__':

    #exemplo 
    def f(x, y):
        return y*(2-x)+x+1
    
    x0 = 1.65835
    y0 = 0.30861 
    h = 0.13646
    n = 10

    r = ralston(f, x0, y0, h, n)
    i = 0
    for (a,b) in r:
        i+=1
        print(f'x_{i} = {a}\ny_{i} = {b}\n')