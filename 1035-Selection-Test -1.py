
def main():
	# entrada
	numero = input("")

	# calculos, operacoes, processamento
	valores = numero.split()	
	a, b, c, d = valores

	if int(b) > int(c) and int(d) > int(a) and int(c) + int(d) > int(a) + int(b) and int(c) > 0 and int(d) > 0 and int(a) % 2 == 0:
		print("Valores aceitos")
	else:
		print("Valores nao aceitos") 

	
if __name__ == '__main__':
	main()