class overloading():
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def multiple(self):
        A = self.a*self.b*self.c

        print("multiplication of the number:" ,A)
    def multiplication(self):
        B = self.a*self.b*self.c*self.d
        print("multiplication of the number:",B)

multiply=overloading(4,5,6,7)
multiply.multiplication()
multiply.multiple()



