t=t=([[-1 for j in range(100)] for i in range(100)])

def func(l,val,w,n,g=0):
    if w==0 or n==0:
        return 0
    if t[n][w]!=-1:
        print(t[n][w])
        return t[n][w]
    
    elif (l[n-1]<=w):
        t[n][w]=(max(val[n-1]+func(l,val,w-l[n-1],n-1),func(l,val,w,n-1)))
        return t[n][w]
    else:
        t[n][w]=func(l,val,w,n-1)
        return t[n][w]

print(func([1,3,4,5],[1,4,5,7],10,4))
