class overloading():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        real=self.a + other.a
        imaginary=self.b + other.b
        return (real ,imaginary)




A=overloading(2,6)
B=overloading(3,9)
print("addition of two number is :", A + B)