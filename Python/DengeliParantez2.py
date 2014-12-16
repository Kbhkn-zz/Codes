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

def parChecker(String):
    s, denge, index = Stack(), True, 0
    while index < len(String) and denge:
        sembol = String[index]
        if sembol in "([{":
            s.push(sembol)
        else:
            if s.isEmpty():
                denge = False
            else:
                top = s.pop()
                if not kontrol(top,sembol):
                    denge = False
        index += 1
    if denge and s.isEmpty():
        return "Parantezler dengeli."
    elif denge:
        return "Parantezler dengeli değil: Parantez kapatılmamış."
    else:
        return "Parantezler dengeli değil: Parantez açılmamış"

def kontrol(acik,kapali):
    acilanlar,kapananlar = "([{",")]}"
    if acik in acilanlar: x= True
    if kapali in kapananlar: y=True
    return x == y

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
print(parChecker('[()]}'))