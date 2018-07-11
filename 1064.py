
def main():
	
	# entradav
	soma=0	
	cont=0
	i=1
	while i<=6:
		valor=float(input())
		if valor>=0:
			soma=soma+valor
			cont=cont+1
		i=i+1
	print("%i valores positivos\n%.1f" % (cont, soma/cont))
	

if __name__ == '__main__':
	main()
