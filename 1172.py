vetor = []
for i in range(10):
    vetor += [input()]

for i in range(len(vetor)):
    if int(vetor[i]) <= 0:
        vetor[i] = 1
        print("X[%d] = %d" % (i, vetor[i]))
    else:
        print("X[%d] = %d" % (i, int(vetor[i])))
