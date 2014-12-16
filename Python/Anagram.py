def AnagramKonrol(kelime1,kelime2):
    Liste1, Liste2, pos, Kontrol = list(kelime1), list(kelime2), 0, True
    Liste1.sort()
    Liste2.sort()

    while pos < len(kelime2) and Kontrol:
        if Liste1[pos]==Liste2[pos]:
            pos += 1
        else:
            Kontrol = False

    return Kontrol

print(AnagramKonrol("algoritma","logaritma"))
print(AnagramKonrol("Kalıtımsal","Kısaltılma"))
print(AnagramKonrol("hakan","kagan"))