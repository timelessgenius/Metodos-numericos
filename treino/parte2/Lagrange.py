import sympy as sp

def Lagrange(x,y,n,polinomio):
    X = sp.symbols('x')
    for i in range(n):
        c = 1
        d = 1
        for j in range(n):
            if i != j:
                c *= (X-x[j])
                d *= (x[i] - x[j])
        polinomio += y[i]* (c/d)
    return polinomio


polinomio = 0

x = [-1,0,1]
y = [0.54,1,0.54]

n = len(x)

print(sp.expand(Lagrange(x,y,n,polinomio)))