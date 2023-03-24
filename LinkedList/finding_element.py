class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def println(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def search(self,val):
        if self.head is None:
          print("empty...")
        flag=pos=0
        ptr=self.head
        while ptr:
            pos=pos+1
            if(ptr.data==val):
                 print('{} is present at loc {}'.format(val,pos))
                 flag=1
                 ptr=ptr.next 
            if flag==0:
                 print(val,"not present")
if __name__=="__main__":

     list=LinkedList()
     list.head=Node(10)
     second=Node(60)
     third=Node(4)
     list.head.next=second
     second.next=third                      
     print("")
     list.search(10)