class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def baseConverter(Sayi,taban):
    rakamlar = "0123456789ABCDEF"
    remstack = Stack()
    while Sayi > 0:
        kalan = Sayi % taban
        remstack.push(kalan)
        Sayi = int(Sayi / taban)
    yenisayi = ""
    while not remstack.isEmpty():
        yenisayi = yenisayi + rakamlar[remstack.pop()]
    return yenisayi

print(baseConverter(26,16))