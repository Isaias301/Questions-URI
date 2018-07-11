def main():
    n = int(input())
    string = []
    cont = 0
    cont_grupo = 0
    res = ""
    for i in range(1, n*3+n):
        cont += 1
        if cont == 4:
            cont = 0
        else:
            string.append(str(i))
    for grupo_de_tres in string:
        cont_grupo += 1
        if cont_grupo == 3:
            res += grupo_de_tres+'/'
            cont_grupo = 0
        else:
            res += grupo_de_tres+' '
    a = res.split("/")
    a.remove('')
    for i in a:
        print("{} PUM".format(i))

if __name__ == '__main__':
    main()
