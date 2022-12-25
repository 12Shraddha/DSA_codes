class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def print_ll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    
    def add(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node

    def EvenThenOdd(self):
        s=""
        f=""
        node=self.head
        while(node):
            if (node.data)%2==0:
                s+=str(node.data)+" "
            else:
                f+=str(node.data)+" "
            node=node.next
        return(s+f)

llist=Linkedlist()
llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
llist.print_ll()
print(end="\n")
print(llist.EvenThenOdd())
