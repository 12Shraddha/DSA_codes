class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def storeArr(root,arr):
    if root is None:
        return
    storeArr(root.left,arr)
    arr.append(root.data)
    storeArr(root.right,arr)
    return arr


root=Node(50)
root.right=Node(70)
root.right.left=Node(60)
root.right.right=Node(80)
root.left=Node(40)
root.left.left=Node(30)


def funcPrecedorSucc(root,key):
    arr=[]
    arr=storeArr(root,arr)
    pre=None
    succ=None
    if arr[-1]==key:
        pre=arr[-2]
    elif arr[0]==key:
        succ=arr[1]

    for i in range(1,len(arr)-1):
        if arr[i]==key:
            pre=arr[i-1]
            succ=arr[i+1]
            break
    for i in range(0,len(arr)-1):
        if  (arr[i]<key and arr[i+1]>key):
            succ=arr[i+1]
            pre=arr[i]
            break
    
    print("predecessor : ",pre)
    print("Successore : ",succ)

key=60
funcPrecedorSucc(root,key)
    
