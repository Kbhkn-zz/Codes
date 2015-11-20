def listeCarp(Liste):
   if len(Liste) == 1:
        return Liste[0]
   else:
        return Liste[0] * listeCarp(Liste[1:])

print(listeCarp([1,3,5,7,9]))
