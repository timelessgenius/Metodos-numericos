import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def prod_internoD(v1,v2):
    soma = 0
    tam = len(v1)
    for k in range(tam):
        soma+= v1[k]*v2[k]
    return soma

def prod_internoC(v1,v2,variavel,limite_inferior,limite_superior):
    ans = sp.integrate(v1*v2,(variavel,limite_inferior,limite_superior))
    return ans
            
def matriz_prodInternoD(phis):
    tam = len(phis)
    mat = np.zeros((tam,tam))
    for i in range(tam):
        for j in range(tam):
            mat[i][j] = prod_internoD(phis[i],phis[j])
    return mat

def matriz_prodInternoC(phis,x,a,b):
    tam = len(phis)
    mat = np.zeros((tam,tam))
    for i in range(tam):
        for j in range(tam):
            mat[i][j] = prod_internoC(phis[i],phis[j],x,a,b)
    return mat

def mqDiscreto(xs,ys,f_x):
    x = sp.symbols('x')
    m = len(xs) 
    n = len(f_x) 
    phis = np.zeros((n,m))
    fs = []

    for j in range(n):
        fs.append(sp.lambdify(x,f_x[j])) 

    for i in range(n):
        for j in range(m):
            phis[i][j] = fs[i](xs[j])

    # print(phis)

    mat = matriz_prodInternoD(phis)

    # print("\n")

    # print(mat)

    B = np.zeros(n)

    for i in range(len(fs)):
        B[i] = prod_internoD(phis[i],ys)

    # print("\n")

    # print(B)


    ans = np.linalg.solve(mat,B)

    # print(ans)

    polinomio = 0

    for i in range(n):
        polinomio+= ans[i]* f_x[i]

    # print(sp.expand(polinomio))
    return polinomio

def mqContinuo(f,f_x,a,b):
    n = len(f_x) 

    mat = matriz_prodInternoC(f_x,x,a,b)

    # print(mat)

    B = np.zeros(n)

    for i in range(len(f_x)):
        B[i] = prod_internoC(f_x[i],f,x,a,b)

    # print("\n")

    # print(B)


    ans = np.linalg.solve(mat,B)

    # print(ans)

    polinomio = 0

    for i in range(n):
        polinomio+= ans[i]* f_x[i]

    # print(sp.expand(polinomio))
    return polinomio

xs = [0,1,2,3,4,5,6]
ys = [1.1,3.9,5.2,3.3,0.5,-1.2,0.1]
x = sp.symbols('x')
f_x = [1,sp.sin(x),sp.cos(x)]
f = x**2

p = mqDiscreto(xs,ys,f_x)
p2 = mqContinuo(f,f_x,-1,1)



#Gráfico
g1 = sp.lambdify(x, p, 'numpy')
g2 = sp.lambdify(x, p2, 'numpy')
f_num = sp.lambdify(x, f, 'numpy')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
xi = np.linspace(min(xs) - 0.5, max(xs) + 0.5, 400)
ax1.plot(xi, g1(xi) * np.ones_like(xi), color='#2a78d6', linewidth=2, label=f'g(x) = {sp.N(p,4)}')
ax1.scatter(xs, ys, s=60, color='black', edgecolor='white', linewidth=2, zorder=5, label='Pontos da tabela')
ax1.set_title('Mínimos Quadrados: caso discreto', loc='left', fontweight='bold')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(color='#e6e5e0')
ax1.legend(frameon=False, fontsize=8)

xc = np.linspace(-1, 1, 400)
ax2.plot(xc, f_num(xc), color='#2a78d6', linewidth=2, label=f'f(x) = {f}')
ax2.plot(xc, g2(xc) * np.ones_like(xc), color='#eb6834', linewidth=2, label=f'g(x) = {sp.N(p2,4)}')
ax2.set_title('Mínimos Quadrados: caso contínuo', loc='left', fontweight='bold')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.grid(color='#e6e5e0')
ax2.legend(frameon=False, fontsize=8)

plt.tight_layout()
plt.show()