def func(l,val,w,n):
    t=t=([[False for j in range(w+1)] for i in range(n+1)])
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                t[i][j]=0
    # print(t)
    for i in range(1,n+1):
        for j in range(1,w+1):
            if l[i-1]>j:
                t[i][j]=(t[i-1][j])
            else:
                t[i][j]=(max(val[i-1]+t[i-1][j-l[i-1]],t[i-1][j]))
    return(t[n][w])

print(func([1,3,4,5],[1,4,5,7],10,4))

