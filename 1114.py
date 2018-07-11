def main():
	
	while True:
		senha = int(input())
		if senha != 2002:
			print("Senha Invalida")
		elif senha == 2002:
			print("Acesso Permitido")
			break
		
if __name__ == '__main__':
	main()
