class Polinom:
    def __init__(self,Xkare,X,Sabit):
        self.xkare = Xkare
        self.x = X
        self.sabit = Sabit

    def __add__(self, other):
        yxkare = self.xkare + other.xkare
        yx = self.x + other.x
        ysabit = self.sabit + other.sabit
        return Polinom(yxkare,yx,ysabit)

    def __sub__(self, other):
        yxkare = self.xkare - other.xkare
        yx = self.x - other.x
        ysabit = self.sabit - other.sabit
        return Polinom(yxkare,yx,ysabit)

    def __mul__(self, other):
        yxdort = self.xkare * other.xkare
        yxkup = self.xkare*other.x + self.x*other.xkare
        yxkare = self.xkare*other.sabit + self.x*other.x + self.sabit*other.xkare
        yx = self.x*other.sabit + self.sabit*other.x
        ysabit = self.sabit*other.sabit
        return str(yxdort)+ "x^4 + " +str(yxkup) + "x^3 + " +str(yxkare) + "x^2 + " + str(yx) + "x + " + str(ysabit)


    def __str__(self):
        if self.x < 0 and self.sabit < 0:
            return str(self.xkare)+ "x^2 - " +str(-1*self.x) + "x - " +str(-1*self.sabit)
        elif self.x < 0 and self.sabit >=0:
            return str(self.xkare)+ "x^2 - " +str(-1*self.x) + "x + " +str(self.sabit)
        elif self.x >= 0 and self.sabit < 0:
            return str(self.xkare)+ "x^2 + " +str(self.x) + "x - " +str(-1*self.sabit)
        else:
            return str(self.xkare)+ "x^2 + " +str(self.x) + "x + " +str(self.sabit)

a = Polinom(2,3,4)
b = Polinom(4,1,6)
print(a+b)
print(a-b)
print(a*b)