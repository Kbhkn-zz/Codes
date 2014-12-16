def ListeYap(cumle):#return list(cumle) de kullanılabilir.
    Liste = []
    for i in cumle:
        Liste.append(i)
    return Liste

def SesliDondur(cumle):
    Sesliler,SesliHarfler = [], "aeıioöuüAEIİOÖUÜ" #Python -3.4 sürümleri için "aeiouAEIOU" kullanınınız.
    for i in cumle:
        if (i in SesliHarfler) and (i not in Sesliler):
            Sesliler.append(i)
    return Sesliler #"".join(Sesliler)


print(ListeYap("Mustafa Cemal Itır İrem"))
print(SesliDondur("Mustafa Cemal Itır İrem"))

