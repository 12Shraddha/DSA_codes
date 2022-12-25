def func(x,y,n,m):
    t=([[False for i in range(m+1)] for j in range(n+1)])
    
    for  i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j]=0
    
    max_=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+ t[i-1][j-1]
                max_=max(max_,t[i][j])
            else:
                t[i][j]=0
    return max_

def func_(x,y,n,m,g=0,mx=0):
    if n==0 or m==0:
        return mx
    if x[n-1]==y[m-1]:
        mx=max(mx,g+1)
        return (func_(x,y,n-1,m-1,g+1,mx))
    else:
        return(max(func_(x,y,n,m-1,0,mx),func_(x,y,n-1,m,0,mx)))


print(func_("iabdxyze","habxyzsdde",8,10))
print(func("abcdxyze","xyzsdde",8,7))