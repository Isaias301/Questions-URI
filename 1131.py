
def main():
	gols_inter, gols_gremio = input().split()
	if int(gols_inter) > int(gols_gremio):
		total_inter = 1
		total_gremio = 0
	elif int(gols_inter) == int(gols_gremio):
		empate = 1
	else:
		total_inter = 0
		total_gremio = 1

	empate = 0
	total_grenal = 1
	
	while True:
		opcao = int(input("Novo grenal (1-sim 2-nao)\n"))
		if opcao == 1:
			gols_inter, gols_gremio = input().split()
			total_grenal += 1
			if int(gols_inter) > int(gols_gremio):
				total_inter += 1
			elif int(gols_inter) == int(gols_gremio):
				empate += 1
			else:
				total_gremio += 1
		elif opcao == 2:
			break

	print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}".format(total_grenal, total_inter, total_gremio, empate))
	if total_inter > total_gremio:
		print("Inter venceu mais")
	elif total_inter == total_gremio:
		print("Nao houve vencedor")
	else: 
		print("Gremio venceu mais")
		
if __name__ == '__main__':
	main()
 