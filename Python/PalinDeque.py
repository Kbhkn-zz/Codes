class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

def palTest(Kelime):
    Liste = Deque()
    Kontrol = True

    for ch in Kelime:
        Liste.addRear(ch)

    while Liste.size() > 1 and Kontrol:
        Fch = Liste.removeFront()
        Lch = Liste.removeRear()
        if Fch != Lch:
            Kontrol = False

    return Kontrol

print(palTest("lsdkjfskf"))
print(palTest("radar"))
print(palTest("12345678900987654321"))