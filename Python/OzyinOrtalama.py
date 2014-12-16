def listeTopla(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + listeTopla(liste[1:])

def hesapla(Liste):
    uzunluk = len(Liste)
    toplam = listeTopla(Liste)
    return toplam/uzunluk

print(hesapla([1,3,5,7,9]))