def main():
    cartas = input().split()
    lista = tranforma_itens_int(cartas)
    print(ordem(lista))


def ordem(lista):
    if lista[0] < lista[1] and lista[1] < lista[2] and lista[2] < lista[3] and lista[3] < lista[4]:
        return "C"
    if lista[0] > lista[1] and lista[1] > lista[2] and lista[2] > lista[3] and lista[3] > lista[4]:
        return "D"
    else:7
        return "D"


def tranforma_itens_int(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista


if __name__ == "__main__":
    main()
