import numpy as np
from math import *
import sympy as sp
import matplotlib.pyplot as plt

A = [-1,0,1]
B = [0.54,1,0.54]

m = np.zeros((3,3), dtype=int)

x = sp.symbols('x')

polinomio = 0

for i in range(len(m)):
    for j in range(len(m)):
        if j == 0:
            m[i][j] = 1
        else:
            m[i][j] = pow(A[i],j)

aux = np.linalg.solve(m,B)

for i in range(len(m)):
    polinomio+=aux[i]*x**i

polinomio = sp.expand(polinomio)

print(polinomio)

f = sp.lambdify(x, polinomio, 'numpy')
xi = np.linspace(min(A) - 0.5, max(A) + 0.5, 400)

plt.plot(xi, f(xi) * np.ones_like(xi), color='#2a78d6', linewidth=2, label=f'P(x) = {polinomio}')
plt.scatter(A, B, s=60, color='black', edgecolor='white', linewidth=2, zorder=5, label='Pontos dados')
plt.title('Método de Vandermonde', loc='left', fontweight='bold')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(color='#e6e5e0')
plt.legend(frameon=False)
plt.show()