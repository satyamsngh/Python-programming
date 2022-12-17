class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add_in_begining(self,data):
        node=Node(data,self.head)
        self.head=node    
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
list=linkedlist()
list.add_in_begining(8)
list.add_in_begining(9)
second=Node(0)
third=Node(4)
list.head.next=second
second.next=third
list.printlist()