def eliminacaoDeGaussPivotamentoParcial(matriz, vetor):

    # Iniciando minha matriz aumentada
    m = []
    tamanho = len(matriz)
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(matriz[i][j])
        linha.append(vetor[i]) # [a00,a01,a02,b0]
        m.append(linha) # [[a00,a01,a02,b2], [...], [...]]


    for i in range(tamanho):
        valor_maior = abs(m[i][i]) # Armazeno o valor do meu possível pivô  ex: valor_maior = abs(elemento00)
        maior_linha = i # Armazeno o valor da minha linha do meu pivô ex: i = 0 (linha 0 onde está meu primeiro elemento da minha matriz aumentada)
        for k in range(i+1, tamanho): # Vou comparar os valores das outras linhas e saber qual é maior, para caso precise eu faça uma troca de linhas
            if abs(m[k][i]) > valor_maior:
                valor_maior = abs(m[k][i])
                maior_linha = k

        if maior_linha != i: # Trocando linhas...
            temp = m[i] # Recebe minha antiga maior linha   ex: temp = [1,0,0]
            m[i] = m[maior_linha] # O índice da minha antiga maior linha recebe minha nova maior linha ex: m[i] = [2,1,2]
            m[maior_linha] = temp # O índice da minha nova maior linha recebe minha antiga maior linha ex: m[maior_linha] = [1,0,0]

        for j in range(i+1, tamanho): # ex: i = 0 -> range(1, tamanho)
            fator = m[j][i]/m[i][i] # ex: fator = elemento10/elemento00
            for k in range(i, tamanho+1): # Vai ajustando as linhas ex: L2' -> L2 - fator*L1
                m[j][k] = m[j][k] - fator*m[i][k]


    ans = tamanho*[0]
    for i in range(tamanho-1, -1, -1):
        soma = 0
        for j in range(i+1, tamanho):
            soma += m[i][j]*ans[j]
        ans[i] = (m[i][tamanho] - soma)/m[i][i]

    return ans


def eliminacaoDeGaussPivotamentoTotal(matriz, vetor):

    # Iniciando minha matriz aumentada
    m = []
    tamanho = len(matriz)
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(matriz[i][j])
        linha.append(vetor[i]) # [a00,a01,a02,b0]
        m.append(linha) # [[a00,a01,a02,b2], [...], [...]]

    # Guardo aqui qual variável (x0, x1, x2...) está hoje em cada coluna,
    # porque toda troca de coluna embaralha a ordem das variáveis
    ordem_variaveis = []
    for i in range(tamanho):
        ordem_variaveis.append(i)

    for i in range(tamanho):
        valor_maior = abs(m[i][i]) # Armazeno o valor do meu possível pivô
        maior_linha = i # linha onde está o maior valor encontrado
        maior_coluna = i # coluna onde está o maior valor encontrado

        for k in range(i, tamanho): # Percorro as linhas restantes...
            for c in range(i, tamanho): # ...e as colunas restantes (sem contar o termo independente)
                if abs(m[k][c]) > valor_maior:
                    valor_maior = abs(m[k][c])
                    maior_linha = k
                    maior_coluna = c

        if maior_linha != i: # Trocando linhas...
            temp = m[i]
            m[i] = m[maior_linha]
            m[maior_linha] = temp

        if maior_coluna != i: # Trocando colunas...
            for linha in m:
                temp = linha[i]
                linha[i] = linha[maior_coluna]
                linha[maior_coluna] = temp
            # A variável que estava na coluna 'maior_coluna' agora está na coluna i
            temp = ordem_variaveis[i]
            ordem_variaveis[i] = ordem_variaveis[maior_coluna]
            ordem_variaveis[maior_coluna] = temp

        for j in range(i+1, tamanho):
            fator = m[j][i]/m[i][i]
            for k in range(i, tamanho+1):
                m[j][k] = m[j][k] - fator*m[i][k]


    ans_embaralhado = tamanho*[0]
    for i in range(tamanho-1, -1, -1):
        soma = 0
        for j in range(i+1, tamanho):
            soma += m[i][j]*ans_embaralhado[j]
        ans_embaralhado[i] = (m[i][tamanho] - soma)/m[i][i]

    # Desfaço o embaralhamento: ans_embaralhado[i] é o valor da variável
    # ordem_variaveis[i], então coloco cada valor na posição certa
    ans = tamanho*[0]
    for i in range(tamanho):
        ans[ordem_variaveis[i]] = ans_embaralhado[i]

    return ans


A = [[2,2,-1],[3,3,1],[1,-1,5]]
b = [3,7,5]

resposta_parcial = eliminacaoDeGaussPivotamentoParcial(A,b)
resposta_total = eliminacaoDeGaussPivotamentoTotal(A,b)

print("Solução (pivotamento parcial):", resposta_parcial)
print("Solução (pivotamento total):", resposta_total)