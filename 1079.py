
def main():
	n = int(input())

	while n > 0:
		a, b, c = input("").split()
		media = (float(a) * 2 + float(b) * 3 + float(c) * 5) / (10)
		print("%.1f" % media )
		n -= 1
if __name__ == '__main__':
	main()
