def Fibonacci(a):
    if a == 0 or a == 1:
        return a
    else:
        return Fibonacci(a-1) + Fibonacci(a-2)

def AltinOran(x):
    s1,s2 = Fibonacci(x),Fibonacci(x+1)
    sonuc = s2/s1
    while sonuc != 1.618033988749895:
        s1 = Fibonacci(x)
        s2 = Fibonacci(x+1)
        sonuc = s2/s1
        print("Fibonacci",x,",Altın oranı:",sonuc)
        x+=1
    print("Altın orana en yakın",x,".sırada yaklaşıldı.")

AltinOran(1)
#print("1 + kök5 bölü 2 ye göre sonuç: ",(1+math.sqrt(5))/2)