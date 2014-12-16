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

def parDenetle(Kelime):
    yigit, denge = Stack(), True
    for i in range(len(Kelime)):
        sembol = Kelime[i]
        if sembol == "(":
            yigit.push(sembol)
        elif yigit.isEmpty():
            denge = False
        else:
            yigit.pop()
    if denge and yigit.isEmpty():
        return "Parantezler dengeli."
    elif denge:
        return "Parantezler dengeli değil: Parantez kapatılmamış."
    else:
        return "Parantezler dengeli değil: Parantez açılmamış"

print(parDenetle('(()(())())'))
print(parDenetle('))(('))
print(parDenetle('(('))