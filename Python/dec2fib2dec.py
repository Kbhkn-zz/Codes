def Fibonacci(a):
    if a == 0 or a == 1:
        return a
    else:
        return Fibonacci(a-1) + Fibonacci(a-2) #Fibonacci değeri döndürüldü.

def Zeck(x):
    i = 1
    while True:
        if(x >= Fibonacci(i) and x < Fibonacci(i+1)):
            break
        i += 1
    return Fibonacci(i) #Tamsayıya yakın en küçük Fibonacci değeri döndürüldü.F(10) = 55 gibi.

def Zeck2(x):
    i = 1
    while True:
        if(x >= Fibonacci(i) and x < Fibonacci(i+1)):
            break
        i += 1
    return (i) #Tamsayıya yakın en küçük Fibonacci değerinin sırası döndürüldü.F(10) gibi.

def Hesapla(n):
    Liste, Liste2,sayi = [], [], n
    while n >= 1:
        Liste.append(Zeck(n)) #Parçalanmış sayı listeye alındı.
        Liste2.append(Zeck2(n))#Parçalanmış sayının Fibonacci sıraları(F(24),F(20) gibi) listeye alındı.
        n -=Zeck(n)
    #print(sayi,"sayısının parçalanmış Fib şekli: ",Liste)
    #print(sayi,"sayısının parçalanmış Fib sırası:",Liste2)
    return Liste2

def dec2fib(n):
    Liste, fib, sayi = Hesapla(n), [], n
    #print(Liste)
    for i in range(Liste[0]-1): fib.append(0) #1.indis büyüklüğünde boş liste yaratıldı.
    for x in Liste: fib[x-2] = 1 #Değerler içindeki Örn=[14,11] tarzı bu değerler liste içerisinde 1 olarak değiştirldi.
    fib.reverse() #Liste tersten olduğu için liste düzeltildi.
    fib2 = ''.join(str(e) for e in fib) #Fonksiyona string olarak yolladığımız için STR yapıldı.
    #print(sayi,"sayısının Fibonacci taban şekli: ",fib2)
    return fib2

def fib2dec(n):
    Liste, deger, deger2, deger3 = [], [], [], 0
    #print("Belleğe alınan binary sayısı:",n)
    for i in n: Liste.append(int(i)) #String olarak alınan sayı integer olarak listeye atıldı.
    Liste.reverse()
    for i in range(len(Liste)):
        if Liste[i] == 1:
            deger.append(i+2) #String olarak alınan sayının Fibonacci Sırası alındı. F(6),F(4) gibi.
    deger.reverse()
    #print("Binary sayısının hesaplanılacak Fib sıraları:",deger)
    for i in deger: deger2.append(Fibonacci(i)) #Üst Fonk. alınan  değeler hesaplandı F(6)=8 gibi.
    #print("Binary sayısının hesaplanılan Fib değerleri: ",deger2)
    deger3 = sum(deger2) #Değerleri alınan Fib.ler liste içinde toplandı.
    #print("Hesaplanılan Fibonacci değerlerinin toplam şekli:",deger3)
    #a = ''.join(list(map(str,(list3)))) = [1,0,1,0,1]'ı '10101' yapar
    return deger3
###########################FONKSİYON DENEME###################
if dec2fib(fib2dec('1001001000101001')) == '1001001000101001':
    print(True)
if fib2dec(dec2fib(2845)) == 2845:
    print(True)