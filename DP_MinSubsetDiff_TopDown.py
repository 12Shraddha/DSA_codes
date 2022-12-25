def func(l,n):
    w=sum(l)
    t=[[0 for i in range(w+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                t[i][j]=True
            elif i==0:
                t[i][j]=False

    for i in range(1,n+1):
        for j in range(1,w+1):
            if l[i-1]<=j:
                t[i][j]=((t[i-1][j-l[i-1]])or t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    
    l=[i for i in range((w+1)//2 +1) if t[n][i]==True]
    mm=1000
    for i in l:
        mm=abs((min(mm,w-2*i)))
    return mm
    
print(func([1,12,5,6,1],3))
#pint(func([1,2,3],3))

