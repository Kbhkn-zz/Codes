def Hanoi(yukseklik,Disk1, Disk2, Disk3):
    if yukseklik > 0:
        Hanoi(yukseklik-1,Disk1,Disk3,Disk2)
        Goster(Disk1,Disk2)
        Hanoi(yukseklik-1,Disk3,Disk2,Disk1)

def Goster(fp,tp):
    print(fp,"diski",tp,"ye götürüldü.")

Hanoi(3,"A","B","C")