class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data

def greaterNumber(root):
    if root is None:
        return
    
    greaterNumber(root.right)
    global sum
    sum=sum+root.val
    root.val=sum-root.val
    print(root.val)
    greaterNumber(root.left)
    return root

        


root=Node(3)
root.right=Node(4)
root.left=Node(1)
sum=0
greaterNumber(root)

