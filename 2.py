def isSafe(maze,i,j):
    N=len(maze)
    if i<N and j<N and maze[i][j]==1:
        return True
    return False
    
res=[[0 for i in range(30)] for j in range(30)]
def mazeEscape(maze,row,col):
    print("Q")
    N=len(maze)
    if row==N-1 and col==N-1:
        return True

    if isSafe(maze,row,col):
        if mazeEscape(maze,row+1,col)==False or mazeEscape(maze,row,col+1)==False:
            return False
    return True
    


def func():
    maze=[[1, 1, 0, 0], 
[0, 1, 0, 0],
[0, 1, 0, 0],
[0, 1, 1, 1]]
    return mazeEscape(maze,0,0)

print(func())



