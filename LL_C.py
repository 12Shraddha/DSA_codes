class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLL:
    def __init__(self):
        self.head=None

def cloop(head):
    if head==None:
        return True
    temp=head.next
    count=0
    while(temp is not None):
        count+=1
        if temp==head:
            return (f"{True}, count: {count}")
        temp=temp.next
    return False
    

llist=CircularLL()
llist.head=Node(1)
llist.head.next=Node(2)
llist.head.next.next=Node(3)
llist.head.next.next.next=llist.head

print(cloop(llist.head.next))



