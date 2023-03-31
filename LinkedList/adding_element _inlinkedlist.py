class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    
    #adding in front

    def beggining(self,dataa):
        nodee=Node(6)
        nodee.next=self.head
        self.head=nodee 

    #addding in between     

    def between(self,prvdata,dataaa):
        newnode=Node(dataaa)
        if self.head is None:
            return
        if self.head != None:
            temp=self.head
            while(temp.data!=prvdata):
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode   
    #adding at reaer         

    def tail(self,newnode):
        node=Node(newnode)
        if self.head is None:
            self.head=node
            return
        n=self.head
        while n.next:
            n=n.next
        n.next=node         

    def printl(self):
        temp=self.head
        while(temp):
            print(temp.data,end="-->")
            temp=temp.next
            
 
list=linkedlist()
list.beggining(2)
list.beggining(6)
list.tail(9)
list.between(9,7)
list.tail(8)
a=list.printl()
print(a)