
def main():
	cobaias = int(input())
	cont = 1
	coelho = 0
	rato = 0
	sapo = 0
	quantidade_cobaia = 0
	
	while cobaias > 0:
		quant_cobaia, tipo = input().split()
		# c = coelho
		# r = rato
		# s = sapo
		quantidade_cobaia += int(quant_cobaia)

		if tipo.lower() == "c":
			coelho += int(quant_cobaia)
		elif tipo.lower() == "r":
			rato += int(quant_cobaia)
		elif tipo.lower() == "s":
			sapo += int(quant_cobaia)

		cobaias -= 1
	print("Total: %i cobaias\nTotal de coelhos: %i\nTotal de ratos: %i\nTotal de sapos: %i\nPercentual de coelhos: %.2f %%\nPercentual de ratos: %.2f %%\nPercentual de sapos: %.2f %%" % (
																																													quantidade_cobaia, 
																																													coelho, 
																																													rato,
																																													sapo,
																																													(coelho*100)/quantidade_cobaia,
																																													(rato*100)/quantidade_cobaia,
																																													(sapo*100)/quantidade_cobaia
																																												 ))

	
if __name__ == '__main__':
	main()

# Percentual
# (numero*100)/total