from det import matrixGenerate

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



# Main