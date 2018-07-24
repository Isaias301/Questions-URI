
def main():
	# entrada
	numeros = input("")
	
	valor = numeros.split()
	crescente = sorted(valor, key=int)
	print("{}\n{}\n{}\n\n{}\n{}\n{}".format(crescente[0], crescente[1], crescente[2], valor[0], valor[1], valor[2]))

if __name__ == '__main__':
	main()
