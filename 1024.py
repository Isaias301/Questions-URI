# regex
import re

vezez = int(input())
cont = 1
while vezez >= cont:
    senha = input()
    texto = ''

    for caractere in senha:
        if re.match("[a-zA-Z]", caractere):
            texto += chr(ord(caractere)+3)
        else:
            texto += caractere

    novo_texto = texto[::-1]
    part1 = novo_texto[0:int((len(novo_texto)/2))]
    part2 = novo_texto[int((len(novo_texto)/2)):]
    r = ''

    for l in part2:
        r += chr(ord(l)-1)
    texto_final = part1+r
    print(texto_final)
    cont += 1

