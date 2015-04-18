def EnSolDugum(agac):
	while agac[1] != []:
		agac = agac[1]
	return agac

def main():
	dizi = ['a', ['b', ['d', [], []], []], ['c', [], ['f', [], []]]]
	dugum = EnSolDugum(dizi)
	print("Dizinin en sol alt düğümü: " + str(dugum))

main()