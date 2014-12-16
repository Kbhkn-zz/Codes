class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self,n=0):
        return self.items.pop(n)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def palTest(Kelime):
    Liste = Stack()
    Kontrol = True

    for ch in Kelime:
        Liste.push(ch)

    while Liste.size() > 1 and Kontrol:
        Fch = Liste.pop()
        Lch = Liste.pop(-1)
        if Fch != Lch:
            Kontrol = False

    return Kontrol

print(palTest("123456789987654321"))
print(palTest("lsdkjfskf"))
print(palTest("radar"))