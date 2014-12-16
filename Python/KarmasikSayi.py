class KarmasikSayi:
    def __init__(self,Reel,Imajiner):
        self.reel = Reel
        self.imaj = Imajiner

    def __add__(self, other):
        yreel = self.reel + other.reel
        yimaj = self.imaj + other.imaj
        return KarmasikSayi(yreel,yimaj)

    def __sub__(self, other):
        yreel = self.reel - other.reel
        yimaj = self.imaj - other.imaj
        return KarmasikSayi(yreel,yimaj)

    def __mul__(self, other):
        yreel = self.reel*other.reel - self.imaj*other.imaj
        yimaj = self.reel*other.imaj + self.imaj*other.reel
        return KarmasikSayi(yreel,yimaj)

    def __truediv__(self, other):
        yreel = (self.reel*other.reel + self.imaj*other.imaj)
        yimaj = (other.reel*self.imaj -self.reel*other.imaj)
        b = (other.reel**2 + other.imaj**2)
        if yimaj < 0:
            return str(yreel)+"/"+str(b)+" - "+str(-1*yimaj)+"/"+str(b)+"i"
        else:
            return str(yreel)+"/"+str(b)+" + "+str(yimaj)+"/"+str(b)+"i"

    def __str__(self):
        if self.imaj<0:
            return str(self.reel)+" - "+str((-1*self.imaj))+"i"
        else:
            return str(self.reel)+" + "+str(self.imaj) + "i"

f1 = KarmasikSayi(4,+77)
f2 = KarmasikSayi(1,-14)

print(f1,"ve",f2,'sayılarının toplama işlevi sonucu:', f1+f2)
print(f1,"ve",f2,'sayılarının çıkarma işlevi sonucu:', f1-f2)
print(f1,"ve",f2,'sayılarının çarpma işlevi sonucu:', f1*f2)
print(f1,"ve",f2,'sayılarının bölme işlevi sonucu:', f1/f2)