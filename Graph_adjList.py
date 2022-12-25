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
    
    def addEdge(self,edge):
        i,j=edge
        self.data[i].append(j)
        self.data[j].append(i)
    
    def removeEdge(self,edge):
        i,j=edge
        self.data[i].remove(j)
        self.data[j].remove(i)
    
g1=Graph(num_nodes,edges)
g1.addEdge((4,2))
g1.removeEdge((4,2))
print(g1)
