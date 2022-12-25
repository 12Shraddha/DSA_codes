class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLL:
    def __init__(self):
        self.head=None
    
    def push(self,data):
        new_node=Node(data)
        if self.head!=None:
            new_node.next=self.head
            new_node.prev=None
            self.head.prev=new_node
        self.head=new_node
    
    def display(self):
        temp=self.head
        count=0
        while(temp):
            print(temp.data)
            temp=temp.next
            count+=1
        print("count: ",count)

    def reverse(self):
        temp=self.head
        while(temp):
            if temp.prev==None:
                pass
            else:
                DoubleLL.push(self,temp.data)
                temp.prev.next.next=temp.next
                temp.next.prev.prev=temp.prev
            temp=temp.next
    
    def insert(self, next_node, new_data):
        self.next_node=next_node
        self.new_data=new_data

        new_node = Node(new_data)

        if next_node.prev==None:
            new_node.prev=None
            new_node.next=next_node
            next_node.prev=new_node
            self.head=new_node
            return
            
        new_node.next = next_node
        new_node.prev = next_node.prev
        next_node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next =new_node
        
    def biotonic(self):
        left=self.head
        right=self.head
        while(right.next):
            right=right.next
        
        while(left!=right and left.prev!=right):
            if left.data<=right.data:
                left=left.next
            else:
                DoubleLL.insert(self,left,right.data)
                right.prev.next=None

                right=right.prev
                # print(left.data,right.data)




llist=DoubleLL()


llist.push(-1)
llist.push(2)
llist.push(4)
llist.push(1)
llist.push(0)
#0142-1

# llist.insert(llist.head,-1)
# llist.display()

llist.reverse()
llist.display()

# llist.biotonic()
# llist.display()


