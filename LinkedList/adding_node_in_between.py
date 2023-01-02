class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def beginning(self,new_data):
        Node=node(new_data)
        Node.next=self.head
        self.head=Node 
         
    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        Node=node(new_data)
        Node.next=prev_node.next
        prev_node.next=node
    def append(self, new_data):
 
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = node(new_data)
 
        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
 
        # 6. Change the next of last node
        last.next =  new_node    
    def printlist(self):
        temp=self.head
        while (temp):
            print(temp.data) 
            temp=temp.next
          
if __name__=='__main__':
    listl=linkedlist()
    listl.append(12)
    listl.beginning(8)
    listl.beginning(9)
    listl.append(11)
    listl.insert_after(listl.head.next,10)
    listl.printlist()
           

