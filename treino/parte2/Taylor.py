import sympy as sp

x = sp.symbols('x')
x_0 = 0
y = sp.exp(x)

n = 2

polinomio = 0

for k in range(n+1):
    op = ((x-x_0)**k)/sp.factorial(k)
    derivada = sp.diff(y,x,k).subs(x,x_0)
    polinomio+= derivada*op

print(sp.expand(polinomio))
