from det import solveDeterminante

def calculateUpperTriangularSystem(matriz,vetor):
    tamanho = len(matriz)
    ans = tamanho*[0]
    for i in range(tamanho-1,-1,-1): # O range tem a sintaxe : (inicio, fim, passo), como um vetor ou lista funciona de 0 até tamanho-1, vamos colocar que ele começa de tamanho-1, que ele vai até o indice -1 (incluir o zero) e que ele vai funcionar na onrdem inversa (decremnto)
        soma = 0
        for j in range(i+1,tamanho):
            soma += matriz[i][j]*ans[j]
        ans[i] = (vetor[i]- soma)/matriz[i][i]
    return ans

if __name__ == "__main__": # essa condicional implica que esse código "main" só será executado se eu executar o arquivo det.py diretamente
    U = [[5,-2,6,1],[0,3,7,-4],[0,0,4,5],[0,0,0,2]]
    b = [1,-2,28,8]

    det = solveDeterminante(U,len(U))

    if det != 0:
        print("O determinante dessa matriz é:", det)
        print(calculateUpperTriangularSystem(U,b))
    else:
        print("Essa matriz não possui solução única")


