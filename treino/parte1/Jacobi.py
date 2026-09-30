from treino.parte1.det import matrixGenerate

def JacobiVerification(matriz):
    n = len(matriz)
    ans = n*[0]
    for i in range(n):
        soma = 0
        for j in range(n):
            if i == j:
                continue
            else:
                if abs(matriz[i][i]) == 0:
                    print("Impossível efetuar a divisão pois existe pelo menos um elemento da diagonal principal que vale zero!")
                    return
                else:
                    soma += abs(matriz[i][j])/abs(matriz[i][i])

        ans[i] = soma

    return max(ans) < 1

def Jacobi(matriz, vetor, tolerancia, iteracoes):
    n = len(matriz)

    x = n*[0]

    for k in range(iteracoes):
        novo_x = n*[0]

        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += matriz[i][j] * x[j]
            novo_x[i] = (vetor[i] - soma)/matriz[i][i]


        erro = 0

        for i in range(n): 
            dif = abs(novo_x[i] - x[i])
            if dif > erro:
                erro = dif

        x = novo_x

        print(f"Iteração {k+1}: {x}  (erro = {erro})")

        if erro < tolerancia:
            break
    
    return x


# Main

A = [[10,2,1],[1,5,1],[2,3,10]]
b = [7,-8,6]

if JacobiVerification(A):
    print("Critério das linhas satisfeito, o método converge!\n")
    resposta = Jacobi(A,b,0,100)
    print("\nSolução aproximada:", resposta)
else:
    print("Critério das linhas não satisfeito, o método pode não convergir!")