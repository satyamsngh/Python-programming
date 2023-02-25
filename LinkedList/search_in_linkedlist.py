class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def push(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def printl(self):
        v=[]
        n=21

        temp=self.head
        while temp:
            v.append(temp.data)
            temp=temp.next
        if n in v:
            print("yes")
        else:
            print("no")    
    
list=linkedlist()
list.push(9)
list.push(21) 
list.push(2) 
list.push(22) 
list.push(6)
list.printl()
print()

