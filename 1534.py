def main():
    while True:
        try:
            tamanho = int(input())
            a = nova_matriz(tamanho, tamanho)
        except:
            break

        for i in range(len(a)):
            for j in range(len(a[i])):
                print(a[i][j], end='')
            print("")


def nova_matriz(colunas, linhas):
    # crio a matriz
    matriz = ["1"] * colunas

    # crio as colunas
    for i in range(len(matriz)):
        matriz[i] = ["1"] * colunas

    # faço o tratamento para as posições variar de 1 a 3
    b = colunas-1
    for i in range(len(matriz)):

        for j in range(len(matriz[i])):
            if i == j:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 3
            if j == b:
                matriz[i][j] = 2
        b -= 1
    return matriz


if __name__ == '__main__':
    main()
