frase = input()
r = ""
for i in frase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        r = r+"#"
    else:
        r = r+i
print(r[::-1])
