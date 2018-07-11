
def main():
	# entrada
	valor_flutuante = float(input(""))

	# calculos, operacoes, processamento
	if valor_flutuante >= 0 and valor_flutuante <= 25:
		print("Intervalo [0,25]")
	elif valor_flutuante > 25 and valor_flutuante <= 50:
		print("Intervalo (25,50]")
	elif valor_flutuante > 50 and valor_flutuante <= 75:
		print("Intervalo (50,75]")
	elif valor_flutuante > 75 and valor_flutuante <= 100:
		print("Intervalo (75,100]")
	elif valor_flutuante < 0 or valor_flutuante > 100:
		print("Fora de intervalo")
	
if __name__ == '__main__':
	main()