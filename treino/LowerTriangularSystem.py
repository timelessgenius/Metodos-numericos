def calculateLowerTriangularSystem(matriz,vetor):
    n = len(matriz)
    ans = n*[0] # as minhas respectivas incognitas (x1,x2,x3,...,xn)
    for i in range(n): 
        soma = 0
        for j in range(n):
            soma+= L[i][j]*ans[j]
        ans[i] = (b[i] - soma)/L[i][i]
    return ans

# n = 4 # tamanho da matriz nxn
L = [[2,0,0,0],[4,3,0,0],[1,2,5,0],[3,1,2,4]] # Matriz nxn
b = [4,23,19,29] # os valores do meu vetor b


print(calculateLowerTriangularSystem(L,b))
