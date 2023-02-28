class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    
    def beggining(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    
    def between(self,prev):
        temp=self.head
        while (temp.data!=prev):
            temp=temp.next
        tempp=temp.next
        print(tempp.data)
    
    def printl(self):
        node=self.head
        while node:
            node=node.next
            
list=linkedlist()
list.beggining(6)
list.beggining(8)
list.beggining(4)
list.between(4)
list.printl()
print()