from xmlrpc.client import MAXINT, MININT

def func(l,i,j):
    if i>=j:
        return 0
    
    min=MAXINT
    tmp=0
    for k in range(i,j):
        tmp=func(l,i,k)+func(l,k+1,j) +l[i-1]*l[k]*l[j]
        if min>tmp:
            min=tmp
    return tmp

#i=0
# j=n-1
print(func([10,30,5,60],1,3))