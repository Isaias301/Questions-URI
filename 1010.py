
def main():
    while True:
        try:
            codico_peca1, numero_peca1, valor_unitario_peca1 = input().split()
            codico_peca2, numero_peca2, valor_unitario_peca2 = input().split()
            
            valor_a_pagar = (int(numero_peca1)*float(valor_unitario_peca1)) + (int(numero_peca2)*float(valor_unitario_peca2))

            print("VALOR A PAGAR: R$ {:.2f}".format(valor_a_pagar))
        except:
            break


if __name__ == '__main__':
	main()