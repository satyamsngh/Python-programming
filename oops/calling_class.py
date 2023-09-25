class employee:
    def __init__(self,idd,name):
        self.idd=idd
        self.name=name
        print(self.name,self.idd)
    def printtt(self):
        print(self.idd ,self.name )
class department():
    def __init__(self,idd,name,dep):
        employee.__init__(self,idd,name)
        self.dep=dep
        
    
    def printt(self):
        employee.printtt(self)
        print(self.name,self.idd,self.dep)
a=department(23,"satyam","cse")
a.printt()