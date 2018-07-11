def main():
    num =[]
    string = ""
    string_final = ""
    while True:
        x = int(input())
        if x == 0:
            break
        for numero in range(1, x+1):
           num.append(str(numero))
        for i in num:
            string += i+" "
        r = string.split()
        for j in r:
            string_final += str(j)+" "
        print(string_final)
        num.clear()
        string_final = ""
        string = ""

if __name__ == '__main__':
    main()
