def main():
    caso_teste = int(input())
    vetor = []
    cont = 0
    resultados = []

    for i in range(1, caso_teste+1):
        # string mae
        string_para_teste = list(input())
        print(i+2)
        # casos para teste
        index = 0
        for j in range(i+2):
            vetor = input()

            for l in vetor:
                if l in string_para_teste and string_para_teste.index(l) >= index:
                    print(l)
                    print(string_para_teste)
                    index = string_para_teste.index(l)
                    print(index)
                    cont += 1
                else:
                    pass
            vetor = ''

            if cont == len(vetor):
                resultados += ["Yes"]
            else:
                resultados += ["No"]
            cont = 0
            index = 0


    for n in range(len(resultados)):
        print(resultados[n])


if __name__ == '__main__':
    main()
# 2
# AABBbbbaaaccc
# 3
# Abbc
# Abc
# ABc
# AAbbccdefghiabs
# 4
# abc
# ade
# abg
# abs
