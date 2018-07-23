def main():
    # crio a matriz quadrada
    matriz = nova_matriz(12, 12)
    linha = int(input())
    operacao = input()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = input()

    # somo os itens de uma linha na matriz
    print("%.1f" % soma_linha_matriz(matriz, operacao, linha))


# função para somar os itens de uma linha na matriz
def soma_linha_matriz(matriz, operacao, linha):
    soma = 0
    cont = 0
    for i in range(len(matriz[linha])):
        soma += float(matriz[linha][i])
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
