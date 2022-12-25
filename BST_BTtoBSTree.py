class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

# def countNodes(root):
#     if root is None:
#         return 0
#     return countNodes(root.left)+countNodes(root.right)+1

def storeInorder(root,arr):
    if root is None:
        return
    storeInorder(root.left,arr)
    arr.append(root.data)
    storeInorder(root.right,arr)

def arrToBST(root,arr):
    if root is None:
        return
    arrToBST(root.left,arr)
    root.data=arr[0]
    arr.pop(0)
    arrToBST(root.right,arr)

root=Node(10)
root.left=Node(15)
root.right=Node(11)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)

def BTtoBST(root):
    # n=countNodes(root)
    arr=[]
    storeInorder(root,arr)
    arr.sort()
    return arrToBST(root,arr)

BTtoBST(root)
Inorder(root)
