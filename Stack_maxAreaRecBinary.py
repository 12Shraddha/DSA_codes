def MAH(arr):
    n=len(arr)
    sl=[-1]
    sr=[-1]
    res1=[0 for i in range(n)]
    res2=[0 for i in range(n)]
    res=[0]*n
    for i in range(n):
        #NS to left
        j=i
        while(j>0 and sl[j]>=arr[i]):
            j-=1
        
        res1[i]=j
        if j==0:
            res1[i]=0
        sl.append(arr[i])

        #NearestSmallest to right
        pass
    for i in range(n-1,-1,-1):
        k=n-i-1
        while(k>0 and sr[k]>=arr[i]):
            k-=1
        res2[i]=n-k-1
        if sr[k]==-1:
            res2[i]=n-1
        sr.append(arr[i])
    
    mx=0
    for i in range(n):
        mx=max(mx,abs(res2[i]-res1[i]+1)*arr[i])
    return mx

def func(arr,n,m):
    mx=0
    h=[0]*m
    for j in range(m):
        h.append(arr[0][j])
        mx=max(mx,MAH(h))
    
    for i in range(1,n):
        for j in range(m):
            if arr[i][j]==0:
                h[j]=0
            else:
                h[j]+=(arr[i][j])
        mx=max(mx,MAH(h))
    return mx
print(func([[0,1,1,0],[1,1,1,1,1],[1,1,1,1],[1,1,0,0]],4,4))