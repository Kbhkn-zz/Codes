def obeb(sayi1,sayi2):
    while sayi2!=0:
        sayi1, sayi2 = sayi2, sayi1%sayi2
    return sayi1

print(obeb(27,15))