def func(l,w,n):
    if w==0:
        return True
    elif n==0 and w!=0:
        return False
    else:
        if l[n-1]>w:
            return (func(l,w,n-1))
        elif l[n-1]==w:
            return True
        else:
            return (func(l,w-l[n-1],n-1) or func(l,w,n-1))  

# print(func([1,3,7,8,9],10,5))
print(func([1,3,2],2,3))