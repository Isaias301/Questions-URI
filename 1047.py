
def main():
	
	# entrada
	hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()

	# calculos, operacoes, processamento
	hora_inicial = int(hora_inicial)
	minuto_inicial = int(minuto_inicial)
	hora_final = int(hora_final)
	minuto_final = int(minuto_final)

	print(hora_final-hora_inicial)
	print(minuto_final-minuto_inicial)
			

if __name__ == '__main__':
	main()
