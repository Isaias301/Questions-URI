
import math
def main():

	# entrada
	a, b, c = input("").split()
	
	# Processamento
	a = float(a)
	b = float(b)
	c = float(c)
	if a==0 or b*b - 4*a*c < 0:
		print("Impossivel calcular")
	else:
		r1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
		print("R1 = %.5f" % (r1))
		r2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
		print("R2 = %.5f" % (r2))

if __name__ == '__main__':
	main()
