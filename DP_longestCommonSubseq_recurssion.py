def func(l1,l2,n,m):
    if n==0 or m==0:
        return 0
    else:
        if l1[n-1]==l2[m-1]:
            return (1+func(l1,l2,n-1,m-1))
        else:
            return max(func(l1,l2,n,m-1), func(l1,l2,n-1,m))

print(func("abcdh","abedhr",5,6))