def main():
    valor = int(input())

    vetor = [None]*1000
    cont = 0
    for i in range(len(vetor)):
        if cont == valor:
            cont = 0
        vetor[i] = cont
        print("N[{}] = {}".format(i, vetor[i]))
        cont += 1


if __name__ == '__main__':
    main()
