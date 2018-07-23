def main():
    matriz = nova_matriz(3,3, "1")
    mostra_matriz(matriz)
    print(soma_diagonal_principal(matriz))


def nova_matriz(colunas, linhas, valor_padrao):
    matriz = [valor_padrao] * colunas
    for i in range(len(matriz)):
        matriz[i] = [valor_padrao] * colunas
    return matriz


def mostra_matriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])


def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                soma += int(matriz[i][j])
    return soma


# def soma_diagonal_secundaria(matriz):
#     soma = 0
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if i == j:
#                 soma += int(matriz[i][j])
#     return soma


if __name__ == '__main__':
    main()
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 111
# 111
# 111
