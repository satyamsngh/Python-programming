class Person():

	def __init__(self):
		self.name = "satyam"

	def parent(self):
		print(self.name)

class Employee():
	def __init__(self):
		self.post ="senior"
	def post(self):	
		print(self.post)
	
		
class subemployee(Person,Employee):
    def __init__(self):
        Person.__init__(self)
        Employee.__init__(self)
        print("derived")
    def child(self):    
        print(self.post,self.name)
s=subemployee()
s.child()
s.parent()