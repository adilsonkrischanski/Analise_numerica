# Metodo de Runge-Kutta
def rungeKutta(f, x0 ,y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 +2 * m2 + 2 * m3 + m4)/6

        # at valores
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r


if __name__ == '__main__':

    #exemplo 
    def f(x, y):
        return y*(1-x)+x+2
    
    x0 = 0.59273
    y0 = 2.21782
    h = 0.10871
    n = 10
    i=0
    r = rungeKutta(f, x0, y0, h, n)
    for (a,b) in r:
        i+=1
        print(f'x_{i} = {a}\ny_{i} = {b}\n')