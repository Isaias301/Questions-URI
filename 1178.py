def main():
    valor = input()
    teste(valor)


def teste(valor):
    vetor = [None]*100

    for i in range(len(vetor)):
        if i == 0:
             vetor[i] = float(valor)
             print("N[%i] = %.4f" % (i, vetor[i]))
        else:
            vetor[i] = vetor[i-1]/2
            print("N[%i] = %.4f" % (i, vetor[i]))


if __name__ == '__main__':
    main()
