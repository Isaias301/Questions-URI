def main():
    # crio a matriz quadrada
    matriz = nova_matriz(12, 12)
    operacao = input()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = input()

    # somo os itens da area_inferiror
    print("%.1f" % area_inferiror(matriz, operacao))


# função para somar os itens da area_inferiror
def area_inferiror(matriz, operacao):
    soma = 0
    cont = 0
    for i in range(7, 11+1):
        for j in range((11-i)+1, (i+1)-1):
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
