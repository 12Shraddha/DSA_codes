class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def insert(root,data):
    if root is None:
        return Node(data)
    if root.val==data:
        return root
    else:
        node=Node(data)
        if root.val>data:
            root.left=insert(root.left,data)
        else:
            root.right=insert(root.right,data)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)
def preOrder(root):
    if root:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)
    pass

def findMin(root):
    if root:
        global current
        current=root
        findMin(root.left)
    return current.val
    
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
r = insert(r, 55)
# (inOrder(r))
print("Preorder:")
preOrder(r)

current=0
print("Min_el",findMin(r))