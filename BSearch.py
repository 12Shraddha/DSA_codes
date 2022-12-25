def func(arr,n,x,l=0,r=0):
    r=n-1
    if l>=r:
        return False
    else:
        mid=l+(r-l)//2
        if arr[mid]==x:
            return True
        else:
            if arr[mid]>x:
                return func(arr,mid-1,x,l,mid-1)
            else:
                return func(arr,n-mid,x,mid+1,r)

print(func([1,2,4,9,11],5,13))