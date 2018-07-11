
def main():
	
	# entrada
	A, B, C = input().split()

	# calculos, operacoes, processamento
	A = float(A)
	B = float(B)
	C = float(C)
	if B-C < A and A < B+C and A-C < B and B < A+C and A-B < C and C < A+B:
		print("Perimetro =", A + B + C)
	else: 
		print("Area =", ((A + B) * C)/2 )
	# saidas
	
if __name__ == '__main__':
	main()
