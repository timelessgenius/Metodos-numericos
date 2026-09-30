import numpy as np
from math import *
import sympy as sp

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

A = np.linalg.solve(m,B)

for i in range(len(m)):
    polinomio+=A[i]*x**i

print(sp.expand(polinomio))