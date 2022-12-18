class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
list=linkedlist()
list.head=Node(2)
second=Node(3)
third=Node(4)
list.head.next=second
second.next=third
list.printlist()                       