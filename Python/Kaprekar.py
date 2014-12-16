def Kaprekar(Baslangic,Max):
    Liste =[]
    if Baslangic <4: Baslangic=4
    print(1,"ile",Max,"arasındaki kaprekar sayılar:")
    for i in range(Baslangic,Max+1,1):
        Kare = i**2
        basamak = len(str(i))
        sonuc3 = len(str(Kare))
        bul = sonuc3 - basamak
        son = int(str(Kare)[bul::])
        ilk = int(str(Kare)[0:bul])
        if i == ilk+son:
            Liste.append(i)
    return Liste

print(Kaprekar(1,10000))