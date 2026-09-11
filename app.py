def criarMatriz(n):
    matriz = []
    for i in  range(n):
        nova_linha = n*[0]
        matriz.append(nova_linha)
    return matriz

def inserirElementos(matriz, n):
    for i in range(n):
        for j in  range(n):
            valor = float(input("Digite o número que você quer colocar dentro da matriz: "))
            matriz[i][j] = valor

def criarSubMatriz(matriz, linha, coluna):
    submatriz = criarMatriz(len(matriz)-1) # crio uma matriz com uma dimensão a menos, ou seja, se eu tenho uma matriz inicial 3x3, eu vou criar uma submatriz 2x2.
    for i in range(len(matriz)):
        if i == linha:
            continue
        for j in range(len(matriz)):
            if j == coluna:
                continue
            submatriz[i][j] = matriz[i][j] # minha sub matriz na posição ij vai receber meu elemento que está na posição ij da minha matriz principal
    return submatriz

def solveDeterminante(matriz):
    tamanho = len(matriz)
    det = 0;
    if tamanho == 1:
        return matriz[tamanho][tamanho]
    elif tamanho == 2:
        return (matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0])




# Main

tamanho = int(input())

m = criarMatriz(tamanho)
inserirElementos(m, tamanho)

print(m)