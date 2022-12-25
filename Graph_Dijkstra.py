import sys
class Graph:
    def __init__(self,vertices):
        self.num_nodes=vertices
        self.graph=[[0 for column in range(vertices)] for row in range(vertices)]

def minDistance(dis,visited):
    #out: minDistance index
    mn=sys.maxsize
    for i in range(len(visited)):
        if visited[i]==False and dis[i]<mn:
            mn=dis[i]
    return dis.index(mn)
   

def Dijkstra(adjMat,s):
    n=len(adjMat)
    visited=[False]*n
    dis=[sys.maxsize]*n
    dis[s]=0
    for _ in range(n):
        x=minDistance(dis,visited)
        visited[x]=True
        print("Index: ",x,end=" ")
        for y in range(n):
            if adjMat[x][y]>0 and visited[y]==False and dis[y]>dis[x]+adjMat[x][y]:
                dis[y]=dis[x]+adjMat[x][y]
    print("Distance: ",dis)
    return 
    



g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

Dijkstra(g.graph,0)