def deterninant(matris,boyut):
	if (boyut==1):
		return matris[0][0]
	elif(boyut==2):
		return (matris[0][0]*matris[1][1] - matris[0][1]*matris[1][0])	
	else:
		i,t,toplam=1,0,0
		while t<=boyut-1:
			d,t1={},1
			while t1<=boyut-1:
				m,d[t1]=0,[]
				while m<=boyut-1:
					if (m!=t):
						d[t1].append(matris[t1][m])
					m+=1
				t1+=1
			l1=[d[x] for x in d]
			toplam+=i*(matris[0][t])*(deterninant(l1,boyut-1))
			i, t = -i, t+1
		return toplam

print(deterninant([[2312,2]],1))
print(deterninant([[1,2],[65,7]],2))
print(deterninant([[1,2,3],[33,4,51],[65,7,28]],3))
print(deterninant([[1,2,3,23],[33,14,53112,223],[123213,65,7,28],[123,53,643,123]],4))
print(deterninant([[1,2,3,23,4],[12,33,14,53112,223],[41,123213,65,7,28],[213,123,53,643,123],[123,4533,123,0,0]],5))