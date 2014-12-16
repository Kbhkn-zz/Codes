def Hesapla(Sayi):
    tekrar=0
    while Sayi != "6174":
        Bsayi = "".join(sorted(Sayi, reverse=True)) #Büyükten küçüğe doğru sıralandı.
        Ksayi = "".join(sorted(Sayi)) #Küçükten büyüğe doğru sıralandı.
        Sayi = str(int(Bsayi) - int(Ksayi)) #Büyükten küçük çıkartıldı.
        tekrar += 1 #Tekrar sayısı belirlendi.
    return tekrar

num = input("Rakamları farklı dört basamaklı sayi: ")
print("6174 sayısına",Hesapla(num),"denemede ulaşıldı")