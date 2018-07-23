def main():
    vetor = []
    for i in range(20):
        vetor += [int(input())]

    a = []
    for i in range(10, len(vetor)):
        a += [vetor[i]]

    b = []
    t = len(a)-1
    while t >= 0:
        b += [a[t]]
        t -= 1

    c = []
    for i in range(10):
        c += [vetor[i]]

    d = []
    e = len(c)-1
    while e >= 0:
        d += [c[e]]
        e -= 1

    r = b+d
    for l in range(len(r)):
        print("N[{}] = {}".format(l, r[l]))


if __name__ == '__main__':
    main()
