from datetime import datetime
	
def main():
	# entrada
	diaN = int(input("Dia "))
	horaN = input()
	diaF = int(input("Dia "))
	horaF = input()
	
	# processamento
	hhN,mmN,ssN = horaN.split(":")
	hhF,mmF,ssF = horaF.split(":")

	data1 = datetime(2015,8,int(diaN),int(hhN),int(mmN),int(ssN))
	data2 = datetime(2015,8,int(diaF),int(hhF),int(mmF),int(ssF))

	difdata = data2 - data1
	datatt = '{0}:{2}'.format(*str(difdata).split())

	W,X,Y,Z = datatt.split(":")

	# saidas
	print("%s dia(s)" %int(W))
	print("%s hora(s)" %int(X))
	print("%s minuto(s)" %int(Y))
	print("%s segundo(s)" %int(Z))

if __name__ == '__main__':
	main()
