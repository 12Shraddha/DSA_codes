#count the number of subset for which diff in subset is given.
#suppose w=1 and l=[1,2,3,2] so the ans wil be 2
# ({1,2},{2,3}),({1,2},{2,3})
def func(l,w,n):
    s=(sum(l)+w)//2
    sum_array=sum(l)
    t=[[0 for i in range(s+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if j==0:
                t[i][j]=1
            elif i==0:
                t[i][j]=0
    
    for i in range(1,n+1):
        for j in range(1,s+1):
            if l[i-1]<=j:
                t[i][j]=((t[i-1][j-l[i-1]]) + t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    
    return (t[n][s])

print(func([1,1,2,3],1,4))
#print(func([1,3,2,2],1,4))