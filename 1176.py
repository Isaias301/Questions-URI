def main():
    valor = input()
    vetor_fibonaci = fibonaci(int(valor))
    for i in range(int(valor)):
        procura_indixe(int(input()), vetor_fibonaci)


def procura_indixe(indice, vetor):
    for i in range(len(vetor)):
        if int(indice) == i:
            print("Fib({}) = {}".format(indice, vetor[i]))


def fibonaci(valor):
    fibonaci=[0,1]
    p=0
    s=1
    for i in range(valor):
        t=s+p
        fibonaci += [t]
        p=s
        s=t
    return fibonaci


if __name__ == '__main__':
    main()
