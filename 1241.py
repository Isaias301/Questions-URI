quant = int(input())

for i in range(quant):
    a, b = list(map(str,input().split()))
    if a[-len(b):] == b:
        print("encaixa")
    else:
        print("nao encaixa")