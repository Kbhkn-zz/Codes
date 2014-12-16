def ozFaktoriyel(Sayi):
   if Sayi < 2:
        return 1
   else:
        return Sayi * ozFaktoriyel(Sayi-1)

print(ozFaktoriyel(5))