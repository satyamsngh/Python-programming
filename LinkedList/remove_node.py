class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def remove_node(head,n):
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        a=count-n 
        tempp=head
        current=None
        for i in range(a):
            current=tempp
            tempp=tempp.next
        current.next=tempp.next
        tempp.next=None
        del tempp
        return tempp
    def printl(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next       
list=linkedlist()
list.head=node(3)
list.head.next=node(6)
list.head.next.next=node(5)
list.head.next.next.next=node(7)  
linkedlist.remove_node(6,1)
list.printl()

