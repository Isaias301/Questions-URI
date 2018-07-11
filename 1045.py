
def main():
	
	# entrada
	a, b, c = input().split()

	# calculos, operacoes, processamento
	a = float(a)
	b = float(b)
	c = float(c)

	#a2 = a*a
	#b2 = b*b
	#c2 = c*c

	if a >= b+c:
		print("NAO FORMA TRIANGULO")
	else:
		if a**2==b**2+c**2:
			print("TRIANGULO RETANGULO")
		else:
			if a**2>b**2+c**2:
				print("TRIANGULO OBTUSANGULO")
			else:
				print("TRIANGULO ACUTANGULO")
		
		if a==b and b==c:
			print("TRIANGULO EQUILATERO")
		else:
			if a==b or b==c or a==c:
				print("TRIANGULO ISOSCELES")
			
			
if __name__ == '__main__':
	main()
