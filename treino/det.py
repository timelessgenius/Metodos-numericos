def matrixGenerate(n, value=0):
    matriz = [] # crio uma lista
    for i in range(n):
        linha=[] # crio uma sublista chamada linha
        for j in range(n):
            linha.append(value) # adiciono os valores na minha sublista
        matriz.append(linha) # adiciono minha sublista dentro da minha lista
    return matriz # retorno minha lista de listas como uma matriz.

def subMatrixGenerate(m,delete_row, delete_column):
    n = len(m)
    subMatrix = []
    for i in range(n):
        if i == delete_row: # se meu indice for igual da linha que eu quero deletar, eu continuo o loop
            continue
        new_row = [] # crio uma nova linha (auxiliar)
        for j in range(n):
            if j == delete_column: # se meu indice for igual da coluna que eu quero deletar, eu continuo o loop
                continue
            new_row.append(m[i][j]) # adiciono o elemento a[i][j] dentro da minha sub matriz
        subMatrix.append(new_row) # adiciono uma nova linha a minha sub matriz
    return subMatrix

def solveDeterminante(m,n):
    if n == 1:
        return m[n][n]
    elif n == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    else:
        det = 0
        for column in range(n): # percorro todas as colunas da minha matriz principal 
            element = m[0][column] # pego meu elemento a[0][j] e guardo ele para que eu faça o somatorio de todas as dets para achar a det total da matriz 
            submatrix = subMatrixGenerate(m,0,column) # gero uma sub matriz 

            # aqui vou verificar a paridade das colunas, para que o sinal seja alterado conforme sua paridade
            if column % 2 == 0:
                signal = 1
            else:
                signal = -1

            # Realizo o somatório da determinante anterior + sinal x elemento x a determinante da respectiva sub matriz 
            det = det + signal*element*solveDeterminante(submatrix,len(submatrix))
        return det

n = int(input("Digite o tamanho da matriz (n): "))

m = matrixGenerate(n)
for i in range(n):
    for j in range(n):
        m[i][j] = float(input(f"Elemento [{i}][{j}]: ")) 

resultado = solveDeterminante(m,n)
print(m)
print("Determinante:", resultado)




