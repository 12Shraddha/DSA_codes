def func(x,y,n,m,g=0):
    t=([[False for i in range(m+1)] for j in range(n+1)])
    
    if n==0 or m==0:
        return 0
    
    if  t[n][m]!=False:
        return t[n][m]
    
    else:
        if x[n-1]==y[m-1]:
            return (1+func(x,y,n-1,m-1,t[n][m]))
        
        else:
            return max(func(x,y,n,m-1,t[n][m]), func(x,y,n-1,m,t[n][m]))

# print(func("abcdk","abedhr",5,6))

print(func("geek","ekek",4,4))