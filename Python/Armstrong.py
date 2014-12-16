def Armstrong():
    Liste = []

    for i in range(100,1000,1):
        YuzB, OnB, BirB = int(str(i)[2]), int(str(i)[1]), int(str(i)[0])
        YuzKup, OnKup, BirKup = YuzB**3,OnB**3,BirB**3

        if i == YuzKup+OnKup+BirKup:
            Liste.append(i)

    return Liste

print(Armstrong())