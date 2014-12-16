class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(isimlistesi, sayi):
    kuyruk = Queue()
    for isim in isimlistesi:
        kuyruk.enqueue(isim)

    while kuyruk.size() > 1:
        for i in range(sayi):
            kuyruk.enqueue(kuyruk.dequeue())
        kuyruk.dequeue()

    return kuyruk.dequeue()

print(hotPotato(["Hakan","İrem","Mustafa","Yavuz","Ayşe","Cemal"],5))