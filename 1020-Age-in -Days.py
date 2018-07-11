
def main():
	# entrada
	data_nascimento = int(input())
	
	
	# calculos, operacoes, processamento
	anos = data_nascimento/365
	meses = (data_nascimento%365)/30
	dias = (data_nascimento%365)%30

	# saida
	print("%i ano(s)" % anos)
	print("%i mes(es)" %meses)
	print("%i dia(s)" %dias)
	
	
if __name__ == '__main__':
	main()