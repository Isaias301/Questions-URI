def main():
    vetor = []
    for i in range(100):
        vetor += [input()]

    for j in range(len(vetor)):
        if float(vetor[j]) <= 10:
            print("A[%i] = %.1f" % (j, float(vetor[j])))


if __name__ == '__main__':
    main()
