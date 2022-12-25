from pyparsing import one_of


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class Double_ll:
    def __init__(self):
        self.head=None
        self.first_node=None
        self.last_node=None

    def add(self,key):
            pass
    def append(self,key):
        new_node=Node(key)
        if self.head==None:
            self.head=new_node
            last_node=new_node
        else:
            temp=self.head
            while(last_node.next):
                