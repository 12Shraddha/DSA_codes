def func(x,n):
    y=x
    t=[[False for  i in range(n+1)] for j in range(n+1)]

    for i in range(n+1):
        if i==0:
            t[i][0]==0 and t[0][i]==0
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if x[i-1]==x[j-1] and i!=j:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    
    return t[n][n]

print(func("aacbbded",8))

