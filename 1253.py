quantidade = int(input())

for i in range(quantidade):
    cifra = input()
    quant = int(input())
    texto = ''
    for l in cifra:
        posicao = ord(l)-quant

        if(posicao < 65):
            texto += chr(91-(65-posicao))
        else:
            texto += chr(ord(l)-quant)
    print(texto)