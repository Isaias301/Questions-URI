n = int(input())
for i in range(n):
    readline = input()
    s = int(len(readline)/2)
    l = list(readline)
    part_1 = l[0:s]
    part_2 = l[s:]
    part_1.reverse()
    part_2.reverse()
    string = "".join(part_1 + part_2)
    print(string)