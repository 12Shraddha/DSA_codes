def func(arr):
    n=len(arr)
    sl=[-1]
    sr=[-1]
    res1=[0 for i in range(n)]
    res2=[0 for i in range(n)]
    res=[0]*n
    #NS to left
    for i in range(n):
        j=i
        while(j>0 and sl[j]>=arr[i]):
            j-=1
        res1[i]=j
        if j==0:
            res1[i]=0
        sl.append(arr[i])

    #NearestSmallest to right
    for i in range(n-1,-1,-1):
        k=n-i-1
        while(k>0 and sr[k]>=arr[i]):
            k-=1
        res2[i]=n-k-1
        if sr[k]==-1:
            res2[i]=n-1
        sr.append(arr[i])
    
    for i in range(n):
        res[i]=abs(res2[i]-res1[i]+1)*arr[i]
    return (res)

print(func([6,2,5,4,5,1,6]))