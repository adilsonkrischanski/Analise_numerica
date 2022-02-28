# Spline method

import numpy as np
import matplotlib.pyplot as plot

def spline(x, y):
    """
    """
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k+1] - x[k] for k in  range(n - 1)}

    A = [[1] + [0] *(n -1)]
    for i in range(1, n-1):
        row = [0]* n
        row[i-1] = h[i-1]
        row[i] =  2*(h[i-1] + h[i])
        row[i+1] = h[i]
        A.append(row)
    A.append([0]*(n-1)+[1])

    B = [0]
    for k in range(1, n - 1):
        row = 3*(a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k-1])/h[k-1]
    B.append(0)

    c = dict(zip(range(n), np.linalg.solve(A,B)))
    # print('Valores dos c\'s ')

    b = {}
    d = {}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        d[k] = (c[k+1] - c[k])/(3*h[k])

    s = {}
    for k in range(n-1):
        eq = f'{a[k]}{b[k]:+}*(x-{x[k]}){c[k]:+}*(x-{x[k]})**2{d[k]:+}*(x-{x[k]})**3'
        s[k] = {'eq': eq, 'domain':[x[k+1]]}

    return s

# (1,1), (2,4), (4,2), (5,3)
x = [1, 2, 4, 5]
y = [1, 4, 2, 3]

eqs = spline(x,y)
print(eqs)

for k, value in eqs.items():
    def p(x):
        return eval(value['eqs'])
    t = np.linspace(*value['domain'], 100)
    plot.plot(t, p(t), label= f"$S_{k}(x)$")

plot.scatter(x,y)
plot.legend()
plot.savefig('spline.png')


# tem erro no np.linalg.solve(A, B)
# mas nao sei arrumar
# entao vai assim msm