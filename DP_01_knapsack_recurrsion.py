#len of l==n
# l is an array of wt
# m is an array of Value
# w is a weight constrain
def func(l,val,w,n):
    if w==0 or n==0:
        return 0
    elif (l[n-1]>w):
        return func(l,val,w,n-1)
    else:
        return (max(val[n-1] + func(l,val,w-l[n-1],n-1),func(l,val,w,n-1)))
        
 
print(func([1,3,4,5],[1,4,5,7],10,4))