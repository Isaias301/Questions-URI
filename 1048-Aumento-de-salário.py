# Autor: Isaias Santana Oliveira

salario = float(input(""))

if salario >= 0 and salario <= 400.00:
	percentual = 15
	reajuste = (percentual / 100) * salario
	novo_salario = reajuste + salario

elif salario >= 400.01 and salario <= 800.00:
	percentual = 12
	reajuste = (percentual / 100) * salario
	novo_salario = reajuste + salario

elif salario >= 800.01 and salario <= 1200.00:
	percentual = 10
	reajuste = (percentual / 100) * salario
	novo_salario = reajuste + salario

elif salario >= 1200.01 and salario <= 2000.00:
	percentual = 7
	reajuste = (percentual / 100) * salario
	novo_salario = reajuste + salario

elif salario > 2.000:
	percentual = 4
	reajuste = (percentual / 100) * salario
	novo_salario = reajuste + salario
	
	
print("Novo salario: %.2f" % novo_salario) 
print("Reajuste ganho: %.2f" % reajuste)
print("Em percentual: %i %%" % percentual) 