def matrixGenerate(n, value=0):
    matriz = [] # crio uma lista
    for i in range(n):
        linha=[] # crio uma sublista chamada linha
        for j in range(n):
            linha.append(value) # adiciono os valores na minha sublista
        matriz.append(linha) # adiciono minha sublista dentro da minha lista
    return matriz # retorno minha lista de listas como uma matriz.

def ReadValuesToMatriz(matriz): # Nessa função eu só vou jogar valores digitados pelo usuário dentro da matriz que tá composta apenas por 0's
    tamanho = len(matriz)
    for i in range(tamanho):
        for j in range(tamanho):
           matriz[i][j] = int(input())


def somatorio(U,L,i,j,limite):
    soma = 0
    for k in range(limite):
        soma += L[i][k] * U[k][j]
    return soma

def LU_Decomposition(m):
    n = len(m) # tamanho da minha matriz inicial
    U = matrixGenerate(n) # Gero uma matriz triangular superior
    L = matrixGenerate(n) # Gero uma matriz triangular inferior

    for i in range(n):
        L[i][i] = 1 # Seto os elementos da diagonal principal da minha matriz triangular inferior como 1 
        for j in  range(i,n): # Vou inserindo os valores na minha matriz triangular superior usando a fórmula que tá no slide 
            U[i][j] = m[i][j] - somatorio(U,L,i,j,i)
        for j in range(i+1,n): # Vou inserindo os valores na minha matriz triangular inferior usando a fórmula que tá no slide 
            L[j][i] = int((m[j][i] - somatorio(U,L,j,i,i))/U[i][i])
    return U,L # Retorno minhas novas matrizes Upper e Lower que foram resultados da decomposição da matriz m (matriz inicial)

# Main

if __name__ == "__main__": # essa condicional implica que esse código "main" só será executado se eu executar o arquivo det.py diretamente

    n = 4

    m = matrixGenerate(n)

    ReadValuesToMatriz(m)

    U,L = LU_Decomposition(m)

    print(U)
    print("\n") 
    print(L)

