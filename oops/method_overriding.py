class A():
    def method(self):
        print("father name is xyz")

class B(A):
    def method(self):
        print("child name is abc")

F=A()
G=B()
F.method()
G.method()

## anothwer example for 