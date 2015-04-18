def Min_Bul(agac):
	enk = agac[0]
	while agac[1] != []:
		agac = agac[1]
		if agac[0] < enk:
			enk = agac[0]
	return enk

def main():
	agac = [5, [4, [3, [], []], []], [2, [], [1, [], []]]]
	dizi =[6 ,[5,[4,[3,[2,[1,[],[]],[]],[]],[]],[]],[]]
	enKucukEleman = Min_Bul(dizi)
	print("Dizinin en küçük elemanı: " + str(enKucukEleman))

main()