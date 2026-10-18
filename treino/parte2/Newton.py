import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def coef(xs, ys):
    n = len(xs)

    c = np.array(ys,dtype=float)

    for i in range(1,n):
        for j in range(n-1,i-1,-1):
            c[j] = (c[j] - c[j-1])/ (xs[j] - xs[j-i])

    return c

def avaliacao(xs,d,z):
    n = len(d)
    p = d[n-1]

    for i in range(n-2,-1,-1):
        p = d[i] + p*(z-xs[i])

    return p


def interpolar(xs,ys,z):
    ans = coef(xs,ys)

    return sp.expand(avaliacao(xs,ans,z))


def acrescentarponto(polinomio, novo_xs, novo_ys, xs,ys):
    # P_n+1 = P_n + prod*f[x0...xn]
    prod = produtorio_aux(xs)

    xs = np.append(xs,novo_xs)
    ys = np.append(ys,novo_ys)

    coef_aux = coef(xs,ys)
    novo_coef = coef_aux[-1]

    novo_p = polinomio + prod*novo_coef

    return sp.expand(novo_p),xs,ys
    


def produtorio_aux(xs):
    z = sp.symbols('x')
    n = len(xs)
    prod = 1

    for i in range(n):
        prod*=(z-xs[i])

    return prod    
    

x = sp.symbols('x')
xs = [-1,0,1]
ys = [0.54,1,0.54]

p = interpolar(xs,ys,x)

print(p)

print("\n")

p_antigo = p

p,xs,ys = acrescentarponto(p,2,-0.42,xs,ys)

print(p)


#Gráfico    
f2 = sp.lambdify(x, p_antigo, 'numpy')
f3 = sp.lambdify(x, p, 'numpy')
xi = np.linspace(min(xs) - 0.5, max(xs) + 0.5, 400)

plt.plot(xi, f2(xi) * np.ones_like(xi), color='#2a78d6', linewidth=2, label=f'Antes: {p_antigo}')
plt.plot(xi, f3(xi) * np.ones_like(xi), color='#eb6834', linewidth=2, label=f'Com ponto novo: {p}')
plt.scatter(xs[:-1], ys[:-1], s=60, color='black', edgecolor='white', linewidth=2, zorder=5, label='Pontos iniciais')
plt.scatter(xs[-1:], ys[-1:], s=60, color='#eb6834', edgecolor='white', linewidth=2, zorder=5, label='Ponto acrescentado')
plt.title('Método de Newton', loc='left', fontweight='bold')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(color='#e6e5e0')
plt.legend(frameon=False, fontsize=8)
plt.show()