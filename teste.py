def main():
    # crio a matriz quadrada
    matriz = nova_matriz(12, 12)
    operacao = input()

    # somo o lado esquerdo da matriz
    matriz = abaixo_da_diagonal_secundaria(matriz, operacao)
    mostra_matriz(matriz)


# função para cria uma matriz
def nova_matriz(colunas, linhas):
    # crio a matriz
    matriz = ["1"] * colunas

    # crio as colunas
    for i in range(len(matriz)):
        matriz[i] = ["1"] * colunas
    return matriz


# mostrar matriz
def mostra_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print(" ")


if __name__ == '__main__':
    main()
