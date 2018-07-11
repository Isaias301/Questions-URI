	
def main():
	# entrada
	n1, n2, n3, n4 = input("").split()
	
	# processamento
	media_aluno = (float(n1)*2 + float(n2)*3 + float(n3)*4 + float(n4)*1)/10
	print("Media: %.1f" % media_aluno)
	if media_aluno >= 7.0:
		print("Aluno aprovado.")
	elif media_aluno < 5.0:
		print("Aluno reprovado.")
	elif media_aluno >= 5.0 and media_aluno <= 6.9:
		print("Aluno em exame.")
		nota_exame = float(input())
		print("Nota do exame: %.1f" % nota_exame)
		media = (nota_exame+media_aluno)/2
		if media >= 5.0:
			print("Aluno aprovado.")
			print("Media final: %.1f" % media)
		else:
			print("Aluno reprovado")
			print("Media final: %.1f" % media)


if __name__ == '__main__':
	main()
