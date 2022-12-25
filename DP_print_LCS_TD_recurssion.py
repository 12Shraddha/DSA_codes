def func_(x,y,n,m,g=""):
    if n==0 or m==0:
        return g
    elif x[n-1]==y[m-1]:
        return (func_(x,y,n-1,m-1,x[n-1]+g))
    else:
        if len(func_(x,y,n,m-1,g))>len(func_(x,y,n-1,m,g)):
            return func_(x,y,n,m-1,g)
        else:
            return func_(x,y,n-1,m,g)
        
def func(x,y,n,m):
    t=([["" for i in range(m+1)] for j in range(n+1)])

    for  i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j]=""
    
    for  i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=t[i-1][j-1]+x[i-1]
            else:
                if len(t[i-1][j])>len(t[i][j-1]):
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i][j-1]
        # print(t[i][j])
    return t[n][m]
print(func_("abcdxyze","xyzsdde",8,7))
print(func_("abcdaf","acbcf",6,5))
print(func("abcdxyze","xyzsdde",8,7))
print(func("abcdaf","acbcf",6,5))

