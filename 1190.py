def main():
    # crio a matriz quadrada
    matriz = nova_matriz(12, 12)
    operacao = input()
    # for i in range(len(matriz)):
    #     for j in range(len(matriz[i])):
    #         matriz[i][j] = input()

    # for i in range(len(matriz)):
    #     for j in range(len(matriz[i])):
    #         print(matriz[i][j], end=' ')
    #     print(" ")

    # somo os itens abaixo da diagonal principal
    matriz = abaixo_da_diagonal_principal(matriz, operacao)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print(" ")

# função para somar os itens abaixo da diagonal principal
def abaixo_da_diagonal_principal(matriz, operacao):
    soma = 0
    cont = 0
    for i in range(1, 10+1):
        for j in range(12-i, 11+1):
            if i < 6:
                matriz[i][j] = "@"
            elif 6 >= i:
                matriz[i][j] = "@"
    return matriz
        # for j in range()
    # verifico se a operação solicitada e soma ou media
    # if operacao == "S":
    #     return soma
    # elif operacao == "M":
    #     return soma/cont


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
