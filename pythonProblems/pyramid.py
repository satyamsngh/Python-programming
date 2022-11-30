class right():
    def __init__(self,n):
        self.n=n
    def toppyramid(self):
        for i in range(self.n):
            for j in range(i+1):
                print("*",end=" ")
            print() 
         
    def bottompyramid(self):
        for i in range(self.n):
            for j in range(self.n-i):
                print("*",end=" ")
            print()    

row_column=right(5)
row_column.toppyramid()
row_column.bottompyramid()