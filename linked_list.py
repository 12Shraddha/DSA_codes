class Node:
    count=0
    def __init__(self,data):
        self.data=data
        self.next=None
        Node.count+=1
    
class Linked_list:
    def __init__(self):
        self.head=None
    
    def print_ll(self):
        count=0
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            count+=1
        print(count)
    
    def add(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_after(self,prev_node,new_data):
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    
    def append(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return
            
        last=self.head
        while(last.next):
            last=last.next
        
        last.next=new_node
    
    def delete_Node(self,key):

        temp=self.head
        if temp==None:
            return
        #if first nodde is the deleting node
        if (temp is not None):
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        
        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        
        prev.next=temp.next
        temp=None
    





llist=Linked_list()

# llist.head=Node(1)
# Second=Node(2)
# Third=Node(3)

# llist.head.next=Second
# Second.next=Third
    
llist.add(1)
llist.add(10)
llist.add(5)
llist.print_ll()
print(Node.count)
# print("After changes")
# (llist.append(21))
# (llist.push(51))
# (llist.insert_after(llist.head.next,100))
# # (llist.print_ll())
# llist.delete_Node(3)
# (llist.print_ll())




