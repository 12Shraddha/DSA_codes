from xmlrpc.client import boolean


def func(n,k):
    if n==1 and k==1:
        return 0
    else:
        mid=2**(n-2)
        if k<=mid:
            return func(n-1,k)
        else:

            return int(not(func(n-1,k-mid)))
    
print(func(4,3))