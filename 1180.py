def main():
    valor = int(input())
    vetor = [None]*valor
    valores = input().split()
    # prenche o vetor criado
    for i in range(len(vetor)):
        vetor[i] = valores[i]

    # recebe o menor valor com sua posição
    menor_posicao = menor(vetor)
    print("Menor valor: {}\nPosicao: {}".format(menor_posicao[0], menor_posicao[1]))


# retorna o maior valor
def maior(vetor):
    r = 0
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if int(r) > int(vetor[j]):
                r = r
            else:
                r = vetor[j]
    return r


# retorna o menor valor com sua posição
def menor(vetor):
    r = maior(vetor)
    p = 0
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if int(r) < int(vetor[j]):
                r = r
            else:
                r = vetor[j]
                p = j
    return r, p



if __name__ == '__main__':
    main()
