
from xmlrpc.client import MAXINT, MININT
t=[[-1 for i in range(100)] for j in range(100)]
def func(l,i,j):
    if i>=j:
        return 0
    
    if (t[i][j]!=-1):
        return t[i][j]

    tmp=MAXINT
    for k in range(i,j):
        tmp=min(tmp,func(l,i,k)+func(l,k+1,j) +l[i-1]*l[k]*l[j])
    t[i][j]=tmp
    return t[i][j]

print(func([10,30,5,60],1,3))

# import sys
# dp = [[-1 for i in range(100)] for j in range(100)]
 
# # Function for matrix chain multiplication
# def matrixChainMemoised(p, i, j):
#     if(i == j):
#         return 0
     
#     if(dp[i][j] != -1):
#         return dp[i][j]
     
#     dp[i][j] = sys.maxsize
     
#     for k in range(i,j):
#         dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
     
#     return dp[i][j]
    

# print(matrixChainMemoised([10,30,5,60],1,3))