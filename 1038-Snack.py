
def main():
	# entrada
	dados = input("")

	# calculos, operacoes, processamento
	codido_e_preco = dados.split()
	"""
		x = codigo do produto
		y = quantidade desejado do produto
	"""
	x, y = codido_e_preco 

	if int(x)==1:
		total = 4.00*float(y)
	elif int(x)==2:
		total = 4.50*float(y)
	elif int(x)==3:
		total = 5.00*float(y)
	elif int(x)==4:
		total = 2.00*float(y)
	elif int(x)==5:
		total = 1.50*float(y)

	# saidas
	print("Total: R$ %.2f" % total) 

if __name__ == '__main__':
	main()