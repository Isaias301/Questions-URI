def main():

	# entradas
	valor = int(input())

	# processamento
	horas = valor/3600
	minutos = (valor%3600)/60
	segundos = (valor%3600)%60
	
	# saida
	print("%i:%i:%i" %(horas, minutos, segundos))
	
if __name__ == '__main__':
	main()