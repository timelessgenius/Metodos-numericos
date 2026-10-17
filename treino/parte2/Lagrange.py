import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

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

p = sp.expand(Lagrange(x,y,n,polinomio))

print(p)

f = sp.lambdify(sp.symbols('x'), p, 'numpy')
xi = np.linspace(min(x) - 0.5, max(x) + 0.5, 400)

plt.plot(xi, f(xi) * np.ones_like(xi), color='#2a78d6', linewidth=2, label=f'P(x) = {p}')
plt.scatter(x, y, s=60, color='black', edgecolor='white', linewidth=2, zorder=5, label='Pontos dados')
plt.title('Método de Lagrange', loc='left', fontweight='bold')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(color='#e6e5e0')
plt.legend(frameon=False)
plt.show()
