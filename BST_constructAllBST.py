class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def preorder(root) :
     
    if (root != None) :
     
        print(root.data, end = " " )
        preorder(root.left)
        preorder(root.right)

def constructBST(start,end):
    list=[]
    if start>end:
        list.append(None)
        return list
    for i in range(start,end+1):
       
        
        leftSubtree=constructBST(start,i-1)
        rightSubtree=constructBST(i+1,end)  
        
        for j in range(len(leftSubtree)) :
            left = leftSubtree[j]
            for k in range(len(rightSubtree)):
                right = rightSubtree[k]
                node = Node(i)   # making value i as root
                node.left = left    # connect left subtree
                node.right = right    # connect right subtree
                list.append(node)
         
           
    return list
n=3
totalTreesFrom1toN = constructBST(1, 3)
for i in range(len(totalTreesFrom1toN)):
    preorder(totalTreesFrom1toN[i])
    print()
