def main():
    vetor = []
    for i in range(15):
        vetor += [input()]

    impar_par(vetor)

def impar_par(vetor):
    par = [None] * 5
    impar = [None] * 5
    contp = 0

    for i in range(len(vetor)):
        if contp > 6:
            if int(vetor[i]) % 2 == 0:
                par += [vetor[i]]
                cont += 1
    print(par)


if __name__ == '__main__':
    main()
