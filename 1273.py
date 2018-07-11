count = 0
while True:
    vezes = int(input())
    if vezes == 0:
        break
    names = []
    tamanhos = []
    for i in range(vezes):
        data = input()
        names.append(data)
        tamanhos.append(len(data))
    if count:
            print()
    count += 1
    for j in names:
        print(j.rjust(max(tamanhos)))
