
def main():
	
	# entrada
	key1 = input()
	key2 = input()
	key3 = input()
	
	# calculos, operacoes, processamento
	if key1=="vertebrado":
		if key2=="ave":
			if key3=="carnivoro":
				print("aguia")
			elif key3=="onivoro":
				print("pomba")
		elif key2=="mamifero":
			if key3=="onivoro":
				print("homem")
			elif key3=="herbivoro":
				print("vaca")
	elif key1=="invertebrado":
		if key2=="inseto":
			if key3=="hematofago":
				print("pulga")
			elif key3=="herbivoro":
				print("lagarta")
		elif key2=="anelideo":
			if key3=="hematofago":
				print("sanguessuga")
			elif key3=="onivoro":
				print("minhoca")
	
if __name__ == '__main__':
	main()
