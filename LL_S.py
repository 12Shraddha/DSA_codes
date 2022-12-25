class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    
    def length(self):
        count=0
        temp=self.head
        while(temp):
            count+=1
            temp=temp.next
        return count
    
    def push(self,new_data):
        self.new_data=new_data
        temp=self.head
        new_data=Node(new_data)
        if temp==None:
            self.head=new_data
        else:
            while(temp.next):
                temp=temp.next
            temp.next=new_data
    
    def printll(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    
    def detectLoop(self):
        slow=self.head
        fast=self.head
        flag=False
        
        while(fast.next):
            if slow==fast and flag==True:
                return True
            flag=True
            slow=slow.next
            fast=fast.next.next 
        return False
            





llist=Linkedlist()
llist.push(1)
llist.push(10)
llist.push(90)
# llist.head.next.next.next=llist.head
llist.printll()
print(llist.length())
print(llist.detectLoop())





 
