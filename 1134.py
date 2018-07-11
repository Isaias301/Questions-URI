def main():
    tot_alcool = 0
    tot_gasolina = 0
    tot_diesel = 0

    while True:
        combustivel = int(input())
        if combustivel == 1:
            tot_alcool += 1
        elif combustivel == 2:
            tot_gasolina += 1
        elif combustivel ==3:
            tot_diesel += 1
        elif combustivel == 4:
            break
    print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(tot_alcool, tot_gasolina, tot_diesel))

if __name__ == '__main__':
    main()
