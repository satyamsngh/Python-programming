class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_after(self,prev_node,data):
        Node=node(data)
        Node.next=prev_node.next
        prev_node.next=node
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
listl=linkedlist()
listl.insert_after(2,4)
second=2
third=5
listl.head.next=second
second.next=third 
print(listl.printlist)           

