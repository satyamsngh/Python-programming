class Atm:
    def __init__(self):
        self.pin=""
        self.amount=0

        self.display()

    def display(self):
        
        a=int(input("1.set the pin \n2.press for deposite \n3.press for check balance \n4.press to withdraw the balance"))
        if a==1:
            self.pinn()
        elif a==2:
            self.deposite()
        elif a==3:
            self.balance_check() 
        elif a==4:
            self.withdraw()    

        self.display()           



    def pinn(self):
        b=input("enter pin:\n")   
        self.pin=b
        print("pin is set")

    def deposite(self):
        aa=input("enter the pin:\n")
        if aa==self.pin:
            e=int(input("enter the amount to deposite:\n"))
            self.amount=self.amount+e
        else:
            print("wrong pin")    

    def balance_check(self):
        aa=input("enter the pin:\n")
        if aa==self.pin:
            print("your account balnce is ", self.amount)
        else:
            print("wrong pin")

    def withdraw(self):
        aa=input("enter the pin:\n")
        if aa==self.pin:
            amnt=int(input("enter the amount:\n"))
            if amnt<self.amount:
                print("amount is withdrawl successfully")
                self.amount=self.amount-amnt
                print("your remaning balance is ",self.amount)



         






u=Atm()
    