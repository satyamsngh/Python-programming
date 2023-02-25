class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printl(self):
        count=0
        temp=self.head
        while temp:
            temp=temp.next
            count+=1
        print("length of linkedlist is" ,+ count)

list=linkedlist()
a=list.head=Node(3)
b=Node(4)
c=Node(5)
d=Node(3)
e=Node(7)
a.next=b
b.next=c
c.next=d
d.next=e
list.printl()