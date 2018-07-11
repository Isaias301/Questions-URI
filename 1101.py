
def main():
	
	soma = 0
	string = ""
	while True:	
		m, n = input().split()
		if int(m) < int(n):
			menor = int(m)
			maior = int(n)
		else:
			menor = int(n)
			maior = int(m)

		if int(m) > 0 and int(n) > 0:
			for i in range(menor, maior+1):
				soma += i
				string += str(i)+" "
			print(string+"Sum={}".format(soma))
			soma = 0
			string = ""
		else:
			break
		

if __name__ == '__main__':
	main()
	