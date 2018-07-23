def main():
    # crio a matriz quadrada
    matriz = nova_matriz(12, 12)
    operacao = input()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = input()

    # somo os itens acima da diagonal principal
    print("%.1f" % soma_acima_da_diagonal_principal(matriz, operacao))


# função para somar os itens acima da diagonal principal
def soma_acima_da_diagonal_principal(matriz, operacao):
    soma = 0
    cont = 0
    for i in range(0, 12):
        for j in range(i+1, 12):
            soma += float(matriz[i][j])
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
