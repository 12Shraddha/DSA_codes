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
    
class Bfs:
    def __init__(self,adjlist,root):
        self.adjlist=adjlist
        self.root=root
        self.queue=[]
        self.visited=[False]*(len(adjlist))
        self.parent=[-1]*(len(adjlist))
    
    def bsf(self):
        self.queue.append(self.root)
        self.visited[self.root]=True
        self.parent[self.root]=-1

        while(len(self.queue)!=0):
            j=self.queue.pop(0)
            print(j,end=" ")
            for i in self.adjlist[j]:
                if self.visited[i]==False:
                    self.queue.append(i)
                    self.visited[i]=True
                    self.parent[i]=j
        return(self.parent)
      
    
g1=Graph(num_nodes,edges)
print(g1)
b1=Bfs(g1.data,3)
print("\nparent of bsf",b1.bsf())