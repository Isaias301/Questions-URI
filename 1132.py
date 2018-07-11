
def main():
	x = int(input())
	y = int(input())
	soma = 0
	ma = 0
	me = 0
	if x > y:
		me = y
		ma = x
	else:
		me = x
		ma = y

	for i in range(me, ma+1):
		if i % 13 != 0:
			soma += i
	print(soma)

		
if __name__ == '__main__':
	main()
 