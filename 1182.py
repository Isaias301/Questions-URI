def main():
    # crio a matriz quadrada
    matriz = nova_matriz(12, 12)
    coluna = int(input())
    operacao = input()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = input()

    # somo os itens de soma_uma_coluna
    print("%.1f" % soma_uma_coluna(matriz, operacao, coluna))


# função para somar os itens de soma_uma_coluna
def soma_uma_coluna(matriz, operacao, coluna):
    soma = 0
    cont = 0
    for i in range(len(matriz)):
        soma += float(matriz[i][coluna])
        cont += 1
# verifico se a operação solicitada e soma ou media
    if operacao == "S":
        return soma
    elif operacao == "M":
        return soma/cont


# função para cria uma matriz
def nova_matriz(colunas, linhas):
    # crio a matriz
    matriz = ["1"] * colunas

    # crio as colunas
    for i in range(len(matriz)):
        matriz[i] = ["1"] * colunas
    return matriz


if __name__ == '__main__':
    main()
