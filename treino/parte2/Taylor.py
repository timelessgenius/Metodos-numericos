import sympy as sp

x = sp.symbols('x')

y  = sp.sin(x)*sp.exp(x)

print(sp.diff(y,x))