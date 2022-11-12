class encapsulation():

    def __init__(self):
        
        self.name="satyam"
    def object(self):
        print("print the object:",self.name)

class methods(encapsulation):
    def variables(self):
        print("name of the give encapslation :",self.name)   

b=methods()
b.object()
b.variables()