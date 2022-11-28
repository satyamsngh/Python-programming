class pallindrone():
    def __init__(self,n):
        self.n=n
    def values(self):
        if self.n==self.n[::-1]:
            print(self.n, "is a palinderone")
        else:
            print(self.n,"is not a palindrome") 

value=pallindrone("malalylalam")
value.values()               
