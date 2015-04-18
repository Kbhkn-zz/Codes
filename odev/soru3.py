def quickSort(m, sol, sag):# 5 boyutlu olan diziyi sıralıyorum O(N) geliyor.
    if sag - sol < 2:
        return m

    pivot, i, j = m[sol], sol + 1, sol + 1

    for j in range(j, sag):
        if m[j] < pivot:
            m[j], m[i], i = m[i], m[j], i + 1
        elif m[j] == pivot:
            m[j], m[i] = m[i], m[j]

    m[sol], m[i - 1] = m[i - 1], m[sol]
    m = quickSort(m, sol, i - 1)
    m = quickSort(m, i, sag)

    return m

def medyanSec(liste): #Algoritmada medyan kullandığım için bu fonksiyon medyan seçmeye yarıyor.
    if len(liste) <= 1:
        return liste[0]
    else:
    	return liste[len(liste)//2] if len(liste) % 2 == 0 else liste[(len(liste) + 1)//2]

def pivotSec(m): #Ödevin kritik noktası pivot seçimi olduğundan bu fonksiyon pivot seçimine yarıyor.
    c, i = [], 0

    while i <= len(m) - 1:
        geciciListe, j = [], 0
        while j < 5 and i <= len(m) - 1:
            geciciListe.append(m[i])
            i, j = i + 1, j + 1
        geciciListe = quickSort(geciciListe, 0, len(geciciListe) - 1)
        c.append(medyanSec(geciciListe))

    c = quickSort(c, 0, len(c) - 1)
    medyan = medyanSec(c)

    return medyan

def pozisyonGetir(m, pozisyon): #Pivotu belirlenen listede 'sıralamadan' istenilen elemanın yerini buluyor.
    pivot, i, j = pivotSec(m), 0, 0

    if len(m) <= 1:
        return m[0]
    for j in range(0, len(m)):
        if m[j] < pivot:
            m[j], m[i], i = m[i], m[j], i + 1
        elif m[j] == pivot:
            m[j], m[i] = m[i], m[j]

    #print("İşlem adımları: pivot: " + str(pivot) + " liste: " + str(m))

    if m.index(pivot) == pozisyon:
        return pivot
    elif m.index(pivot) > pozisyon:
        return pozisyonGetir(m[0:i], pozisyon)
    else:
        return pozisyonGetir(m[i:], pozisyon - i)


def Medyan_Bul(liste):# Bu fonksiyon Verilen listenin medyanını buluyor.
	orta = len(liste) / 2 + 0.5
	if  len(liste) % 2 == 0:
		s1, s2 = pozisyonGetir(liste, orta - 1), pozisyonGetir(liste, orta)
		return (s1 + s2) / 2
	else:
		return pozisyonGetir(liste, orta - 1)

#TEST BÖLÜMÜÜÜÜÜÜÜÜÜ

if __name__ == '__main__':
	a = [2, 12, 13, 4, 1, 6, 17, 9, 18, 8, 5, 10, 20, 16, 11, 19, 14, 7, 3]
    # Sıralı a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20]
	b = [7, 5, 9, 13, 8, 1, 6, 2]
    # Sıralı b = [1, 2, 5, 6, 7, 8, 9, 13]
	c = [2, 12, 13, 4, 1, 6, 17, 9, 18]
	d = [1, 3, 5 ,7, 9, 11, 13, 15]
	e = [1, 3, 5 ,7, 9, 11, 13, 15, 17]
	print("a Listesinin medyanı: ", Medyan_Bul(a))
	print("b Listesinin medyanı: ", Medyan_Bul(b))
	print("c Listesinin medyanı: ", Medyan_Bul(c))
	print("d Listesinin medyanı: ", Medyan_Bul(d))
	print("e Listesinin medyanı: ", Medyan_Bul(e))