def func_r(x,y,n,m):
    if m<n:
        x,y=y,x
        n,m=m,n
    t=([[False for i in range(m+1)] for j in range(n+1)])
    
    for  i in range(n+1):
        for j in range(m+1):
            if i==0:
                t[i][j]=j
            elif j==0:
                t[i][j]=i
            elif x[i-1]==y[j-1]:
                t[i][j]=1+ t[i-1][j-1]
            else:
                t[i][j]=1+min(t[i-1][j], t[i][j-1])
    
    i=n
    j=m
    s=""
    while (i*j>0):
        if x[i-1]==y[j-1]:
            s=x[i-1]+s
            i-=1
            j-=1
        else:
            if t[i-1][j]>t[i][j-1]:
                s=y[j-1]+s
                j-=1
            else:
                s=x[i-1]+s
                i-=1
    while(i>0):
        s=x[i-1]+s
        i-=1
    while(j>0):
        s=y[j-1]+s
        j-=1
        pass
    return s,t

print(func_r("geek","eke",4,3))
print(func_r("AGGTAB","GXTXAYB",6,7))