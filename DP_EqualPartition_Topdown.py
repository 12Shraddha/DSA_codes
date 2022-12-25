def func(l,n):
    w=sum(l)
    k=w//2
    t=[[-1 for i in range(k+1)] for j in range(n+1)]
    if w%2!=0:
        return False
    else:
        for i in range(n+1):
            for j in range(k+1):
                if j==0:
                    t[i][j]=True
                elif i==0:
                    t[i][j]=False
        
    for i in range(1,n+1):
        for j in range(1,k+1):
            if l[i-1]>j:
                t[i][j]=t[i-1][j]
        
            else:
                t[i][j]=t[i-1][j] or t[i-1][j-l[i-1]]
    
    return t[n][k]
    
print(func([1,7,11,5],4))



    

        