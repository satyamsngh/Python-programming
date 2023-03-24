class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def palindrone(head):
    start=head
    stack=[]
    ispalindrone=True

    while start!=None:
        stack.append(start.data)
        start=start.next

    while head!=None:
        i=stack.pop() 
        if head.data==i:
            ispalindrone=True
        else:
            ispalindrone=False
            break
        head=head.next 
    return ispalindrone 

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)
 
# Initialize the next pointer
# of every current pointer
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = None
 
# Call function to check
# palindrome or not
result = palindrone(one)
print(result)             

