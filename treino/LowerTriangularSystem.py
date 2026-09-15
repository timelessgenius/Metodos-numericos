from det import solveDeterminante

def calculateLowerTriangularSystem(matriz,vetor):
    n = len(matriz)
    ans = n*[0] # as minhas respectivas incognitas (x1,x2,x3,...,xn)
    for i in range(n): 
        soma = 0
        for j in range(n):
            soma += L[i][j]*ans[j]
        ans[i] = (b[i] - soma)/L[i][i]
    return ans


if __name__ == "__main__": # essa condicional implica que esse código "main" só será executado se eu executar o arquivo det.py diretamente

    # n = 4 # tamanho da matriz nxn
    L = [[2,0,0,0],[4,3,0,0],[1,2,5,0],[3,1,2,4]] # Matriz nxn
    b = [4,23,19,29] # os valores do meu vetor b
    det = solveDeterminante(L, len(L))

    if solveDeterminante(L,len(L) != 0):
        print("A determinante é:", det)
        print(calculateLowerTriangularSystem(L,b))
    else:
        print("Esse sistema não possui uma solução única!")