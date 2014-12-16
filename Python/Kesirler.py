#Coder: Kbhkn
#Kesirlerde 4 işlem yapma.
class Kesir:
    def __init__(self,Pay,Payda):
        self.pay = Pay
        self.payda = Payda

    def __add__(self,DKesir):
        yenipay = self.pay*DKesir.payda + DKesir.pay*self.payda
        yenipayda = self.payda*DKesir.payda
        ortak = Kesir.ebob(yenipay,yenipayda)
        return Kesir(yenipay/ortak,yenipayda/ortak)

    def __sub__(self,DKesir):
        yenipay = self.pay*DKesir.payda - DKesir.pay*self.payda
        yenipayda = self.payda*DKesir.payda
        ortak = Kesir.ebob(yenipay,yenipayda)
        return Kesir(yenipay/ortak,yenipayda/ortak)

    def __mul__(self, DKesir):
        yenipay = self.pay*DKesir.pay
        yenipayda = self.payda*DKesir.payda
        ortak = Kesir.ebob(yenipay,yenipayda)
        return Kesir(yenipay/ortak,yenipayda/ortak)

    def __truediv__(self,DKesir):
        yenipay = self.pay*DKesir.payda
        yenipayda = self.payda*DKesir.pay
        ortak = Kesir.ebob(yenipay,yenipayda)
        return Kesir(yenipay/ortak,yenipayda/ortak)

    def __str__(self):
        return str(self.pay)+"/"+str(self.payda)

    def ebob(s1,s2):
        while s2 != 0:
            s1, s2 = s2, s1%s2
        return s1


f1 = Kesir(1,4)
f2 = Kesir(1,2)

print(f1,"ve", f2, "Kesirlerinin Toplama işlemi sonucu: ",f1+f2)
print(f1,"ve", f2, "Kesirlerinin Çıkarma işlemi sonucu: ",f1-f2)
print(f1,"ve", f2, "Kesirlerinin Çarpma işlemi sonucu: ",f1*f2)
print(f1,"ve", f2, "Kesirlerinin Bölme işlemi sonucu: ",f1/f2)