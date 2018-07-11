numeros = (6,2,5,5,4,5,6,3,7,6)
n = int(input())

for i in range(n):
    total = 0
    valor = input()
    for j in valor:
        total += numeros[int(j)]
    print("{} leds".format(total))
