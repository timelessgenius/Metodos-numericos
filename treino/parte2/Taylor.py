import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
x_0 = 0
y = sp.exp(x)

n = 2

polinomio = 0

for k in range(n+1):
    op = ((x-x_0)**k)/sp.factorial(k)
    derivada = sp.diff(y,x,k).subs(x,x_0)
    polinomio+= derivada*op

polinomio = sp.expand(polinomio)

print(polinomio)



f = sp.lambdify(x, y, 'numpy')
p = sp.lambdify(x, polinomio, 'numpy')
xi = np.linspace(x_0 - 2, x_0 + 2, 400)

plt.plot(xi, f(xi), color='#6b6a64', linestyle='--', linewidth=1.5, label=f'f(x) = {y}')
plt.plot(xi, p(xi) * np.ones_like(xi), color='#2a78d6', linewidth=2, label=f'Taylor grau {n}: {polinomio}')
plt.scatter([x_0], [float(y.subs(x, x_0))], s=60, color='black', edgecolor='white', linewidth=2, zorder=5, label=f'x₀ = {x_0}')
plt.title('Método de Taylor', loc='left', fontweight='bold')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(color='#e6e5e0')
plt.legend(frameon=False)
plt.show()
