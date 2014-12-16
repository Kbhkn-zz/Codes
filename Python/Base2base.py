class Stack:
    def __init__(self):
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def push(self,item):
        self.items.append(item)
 
    def pop(self):
        return self.items.pop()
 
    def peek(self):
        return self.items[len(self.items)-1]
 
    def size(self):
        return len(self.items)
 
 
def taban_donustur(sayi, tabani, hedef_taban):
    sayi = str(sayi)
    liste = list(sayi[::-1])
    h = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    t, sayac, s = 0, 0, Stack()
    for i in liste:
        if i not in h:
            t += (tabani ** sayac) * int(liste[sayac])
            sayac += 1
        else:
            t += (tabani ** sayac) * h[i]
            sayac += 1
   
    rakamlar = "0123456789ABCDEF"
 
    while t > 0:
        r = t % hedef_taban
        s.push(r)
        t = int(t / hedef_taban)
 
    yeniString = ""
    while not s.isEmpty():
        yeniString = yeniString + rakamlar[s.pop()]
    return yeniString

print(taban_donustur(123, 10, 16))