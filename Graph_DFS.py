num_nodes=5
edges=[(0,1),(0,4),(1,4),(1,3),(1,2),(2,3),(3,4)]

class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes=num_nodes
        self.data=[[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self):
        return "\n".join(["{}-> {}".format(i,j) for i,j in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()
    


g1=Graph(num_nodes,edges)
print(g1)

visited=[False]*(len(g1.data))
parent=[-1]*(len(g1.data))  
stack=[]

def dfs(adjmat,root):
    stack.append(root)
    visited[root]=True
    if len(stack)==0:
        return (parent)

    j=stack.pop()
    print(j,end=" ")
    for i in adjmat[j]:
        if visited[i]==False:
            parent[i]=j
            dfs(adjmat,i)           
      
    return 

b1=dfs(g1.data,3)
b1
print("\nparent of dfs",parent)