
def main():
	
	# entrada
	inicio, fim = input().split()

	# calculos, operacoes, processamento
	duracao=0
	inicio = int(inicio)
	fim = int(fim)

	if inicio > fim:
		duracao = (24 + fim) - inicio
		print("O JOGO DUROU %d HORA(S)" % duracao)

	elif inicio < fim:
		duracao = fim - inicio
		print("O JOGO DUROU %d HORA(S)" % duracao)
	else:
		print("O JOGO DUROU 24 HORA(S)")		
			

if __name__ == '__main__':
	main()
