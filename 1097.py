def main():
    i = 1
    cont = 7
    while (i < 10):
        for x in range(3):
            print("I={} J={}".format(i, cont))
            cont += -1
        i += 2
        cont = i + 6


if __name__ == '__main__':
    main()
