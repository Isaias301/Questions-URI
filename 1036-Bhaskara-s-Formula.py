
def main():
	# entrada
	postos_flutuantes = input("")

	# calculos, operacoes, processamento
	pontos = postos_flutuantes.split()	
	a, b, c = pontos

	if int(b) > int(c) and int(d) > int(a) and int(c) + int(d) > int(a) + int(b) and int(c) > 0 and int(d) > 0 and int(a) % 2 == 0:
		print("Valores aceitos")
	else:
		print("Valores nao aceitos") 

	
if __name__ == '__main__':
	main()