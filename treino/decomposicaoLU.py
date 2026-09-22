def decomposicao_lu(A):
    n = len(A)
    
    # Inicialização de matrizes identidade
    U = [[float(A[i][j]) for j in range(n)] for i in range(n)]
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    P = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for i in range(n - 1):
        # 1. Escolha do Pivô 
        indice_pivo = i
        maior_valor = abs(U[i][i])
        for k in range(i + 1, n):
            if abs(U[k][i]) > maior_valor:
                maior_valor = abs(U[k][i])
                indice_pivo = k

        # 2. Troca de Linhas
        if indice_pivo != i:
            
            U[i], U[indice_pivo] = U[indice_pivo], U[i]
            P[i], P[indice_pivo] = P[indice_pivo], P[i]
            
            if i > 0:
                # Troca manual dos multiplicadores na matriz L
                for k in range(i):
                    L[i][k], L[indice_pivo][k] = L[indice_pivo][k], L[i][k]

        if U[i][i] == 0:
            raise ZeroDivisionError("Pivô nulo encontrado. O sistema é singular.")

        # 3. Eliminação Gaussiana (Substitui as operações vetorizadas)
        for j in range(i + 1, n):
            m = U[j][i] / U[i][i]
            L[j][i] = m
            for k in range(i, n):
                U[j][k] -= m * U[i][k]

    return P, L, U

def multiplicacao_matriz_vetor(M, v):
    n = len(v)
    resultado = [0.0] * n
    for i in range(n):
        resultado[i] = sum(M[i][j] * v[j] for j in range(n))
    return resultado

def substituicao_direta(L, b):
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        soma = sum(L[i][k] * y[k] for k in range(i))
        y[i] = b[i] - soma
    return y

def retro_substituicao(U, y):
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(U[i][k] * x[k] for k in range(i + 1, n))
        x[i] = (y[i] - soma) / U[i][i]
    return x

def resolver_sistema(A, b):
    P, L, U = decomposicao_lu(A)
    Pb = multiplicacao_matriz_vetor(P, b)
    y = substituicao_direta(L, Pb)
    x = retro_substituicao(U, y)
    return x


A = [
    [10,  2,  3,  1,  4,  0,  2,  1,  3,  2],
    [ 2,  9,  1,  3,  0,  2,  1,  4,  2,  1],
    [ 3,  1,  8,  2,  1,  3,  0,  2,  1,  4],
    [ 1,  3,  2, 11,  2,  1,  3,  0,  2,  1],
    [ 4,  0,  1,  2, 10,  2,  1,  3,  0,  2],
    [ 0,  2,  3,  1,  2,  9,  2,  1,  3,  0],
    [ 2,  1,  0,  3,  1,  2, 12,  2,  1,  3],
    [ 1,  4,  2,  0,  3,  1,  2, 10,  2,  1],
    [ 3,  2,  1,  2,  0,  3,  1,  2,  9,  2],
    [ 2,  1,  4,  1,  2,  0,  3,  1,  2, 11]
]

b = [28, 25, 25, 26, 25, 23, 27, 26, 25, 27]

print("Matriz L:")
P, L, U = decomposicao_lu(A)
for row in L:
    print(row)
print("\n")

print("Matriz U:")
for row in U:
    print(row)
print("\n")

print("\nSolução do sistema Ax = b:")

resultado = resolver_sistema(A, b)
print(f"Solução final x: {resultado}")