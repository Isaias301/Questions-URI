def main():
    x = int(input())
    z = 0
    while True:
        r = int(input())
        if (r > x):
            break
    soma = x
    cont = 1
    while (soma < r):
        soma += x + cont
        cont += 1
    print(cont)


if __name__ == '__main__':
    main()
