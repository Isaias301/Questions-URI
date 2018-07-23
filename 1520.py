def main():
    try:
        vezes = int(input())
        vetor = []
        for i in range(vezes):
            x, y = input().split()
            for j in range(int(x), int(y)+1):
                vetor += [j]
        n_para_procurar = int(input())

        vetor_em_ordem = sorted(vetor)
        posicao = []
        for l in range(len(vetor_em_ordem)):
            if vetor_em_ordem[l] == n_para_procurar:
                posicao += [l]

        if posicao != []:
            print("{} found from {} to {}".format(n_para_procurar, posicao[0], posicao[len(posicao)-1]))
        else:
            print("{} not found".format(n_para_procurar))
    except:
        pass


if __name__ == '__main__':
    main()
