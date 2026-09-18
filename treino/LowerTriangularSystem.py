from det import solveDeterminante

def calculateLowerTriangularSystem(matriz,vetor):
    n = len(matriz)
    ans = n*[0] # as minhas respectivas incognitas (x1,x2,x3,...,xn)
    for i in range(n): 
        soma = 0
        for j in range(n):
            soma += matriz[i][j]*ans[j]
        ans[i] = (vetor[i] - soma)/matriz[i][i]
    return ans


if __name__ == "__main__": # essa condicional implica que esse código "main" só será executado se eu executar o arquivo det.py diretamente

    # n = 4 # tamanho da matriz nxn
    L = [[2,0,0,0],[3,5,0,0],[1,-6,8,0],[-1,4,-3,9]] # Matriz nxn
    b = [4,1,48,6] # os valores do meu vetor b
    det = solveDeterminante(L, len(L))

    if solveDeterminante(L,len(L)) != 0:
        print("A determinante é:", det)
        print(calculateLowerTriangularSystem(L,b))
    else:
        print("Esse sistema não possui uma solução única!")