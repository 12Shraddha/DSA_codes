
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def height(node):
    if node is None:
        return 0
    return (1 + max(height(node.left), height(node.right)))

def diameter(root,res):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)
    
    ldiameter = diameter(root.left,res)
    rdiameter = diameter(root.right,res)

    tmp=max(ldiameter,rdiameter)+1
    ans=max(tmp,lheight + rheight + 1)
    res=max(res,ans)
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

res=-10000
res=(diameter(root,res))
print(res)