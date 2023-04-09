class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printl(self,n):
        count=0
        temp=self.head
        while temp:
            count+=1
            print(temp.data,end='-->')
            temp=temp.next
        print(count)
        a=count-n 
        tempp=self.head
        for i in range(a):
            tempp=tempp.next
        temp.next=temp.next.next    
list=linkedlist()
list.head=node(3)
list.head.next=node(6)
list.head.next.next=node(5)
list.head.next.next.next=node(7)  
list.printl(1)     
