n = int(input())
for i in range(n):
    a = input().replace("·", " ")
    a = a.split()
    texto = ""

    for p in a:
        texto += p[0]
    print(texto)