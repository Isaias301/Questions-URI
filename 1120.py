while True:
    valor, num = input().split()

    if int(valor) == 0 and int(num) == 0:
        break
    aux = 0
    num = list(num)
    lista_final = []
    lista = []

    for i in range(len(num)):
        if valor != num[i]:
            lista.append(int(num[i]))

    for i in lista:
        if aux == 0:
            if i != 0:
                lista_final.append(i)
                aux += 1
        else:
            lista_final.append(i)
            aux += 1

    if sum(lista) == 0:
        print("0")
    else:
        for i in lista_final:
            print(i, end=" ".strip())
        print()