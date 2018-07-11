
def main():
	cont = 1
	maior = 0
	posicao = 0
	while cont <= 100:
		n = int(input())
		if maior < n:
			maior = n
			posicao = cont
		cont += 1

	print("{}\n{}".format(maior, posicao))
	
if __name__ == '__main__':
	main()
