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

def Islem(operator, sayi1, sayi2):
    if operator == "*":
        return sayi1 * sayi2
    elif operator == "/":
        return sayi1 / sayi2
    elif operator == "+":
        return sayi1 + sayi2
    elif operator == "-":
        return sayi1 - sayi2

def postfixEval(postfix):
    Islemler = Stack()
    Liste = postfix.split()

    for i in Liste:
        if i in "0123456789":
            Islemler.push(int(i))
        else:
            sayi2 = Islemler.pop()
            sayi1 = Islemler.pop()
            sonuc = Islem(i,sayi1,sayi2)
            Islemler.push(sonuc)
    return Islemler.pop()

print(postfixEval('7 8 + 3 2 + /'))