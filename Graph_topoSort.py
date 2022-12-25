num_nodes=8
edges=[(0,2),(0,4),(0,3),(1,7),(1,2),(2,5),(3,5),(3,7),(4,7),(5,6),(6,7)]

class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes=num_nodes
        self.matrix=[[0 for i in range(self.num_nodes)] for j in range(self.num_nodes)]
        self.edges=edges
        for i,j in self.edges:
            self.matrix[i][j]=1


g1=Graph(num_nodes,edges)
print("initial matrix: ",g1.matrix) 

def toposort(adjmat):
    topoList=[]
    indegzero={}
    row,col=len(adjmat),len(adjmat)
    for i in range(row):
        indegzero[i]=0
        for j in range(col):
            if adjmat[j][i]==1:
                indegzero[i]+=1
    print("Initial indegree zero dict: ",indegzero)
    
    for i in range(row):
        j=min([k for k in range(row) if indegzero[k]==0])
        topoList.append(j)
        indegzero[j]-=1
        for k in range(col):
            if adjmat[j][k]==1:
                indegzero[k]-=1
    return (topoList)


print("topolist: ",toposort(g1.matrix))