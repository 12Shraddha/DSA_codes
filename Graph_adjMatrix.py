num_nodes=5
edges=[(0,1),(0,4),(1,4),(1,3),(1,2),(2,3),(3,4)]
# matrix=[[0 for i in range(num_nodes)] for j in range(num_nodes)]

class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes=num_nodes
        self.matrix=[[0 for i in range(self.num_nodes)] for j in range(self.num_nodes)]
        self.edges=edges
        for i,j in self.edges:
            self.matrix[i][j]=1
            self.matrix[j][i]=1


g1=Graph(num_nodes,edges)
print(g1)           