def func(arr):
    n=len(arr)
    s=[]
    res=[-1 for i in range(n)]
    for i in range(n-1,-1,-1):
        while(len(s)!=0 and s[-1]<=arr[i]):
            s.pop()

        if len(s)!=0 and s[-1]>arr[i]:
            res[i]=s[-1]

        s.append(arr[i])    
    return res
print(func([3,0,0,1,2,4]))
