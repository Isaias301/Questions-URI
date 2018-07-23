def main():
    valor = int(input())

    vetor = [None]*10
    vetor[0] = valor
    for i in range(1, len(vetor)):
        vetor[i] = vetor[i-1]*2

    for j in range(len(vetor)):
        print("N[{}] = {}".format(j, vetor[j]))


if __name__ == '__main__':
    main()
