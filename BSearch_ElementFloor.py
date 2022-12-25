def findFloorEl(arr,k):
    n=len(arr)
    left=0
    right=n-1
    res=-1
    while(left<=right):
        mid=int(left+(right-left)/2)
        if arr[mid]==k:
            return k
        if arr[mid]>k:
            right=mid-1
        else:
            res=max(arr[mid],res)
            left=mid+1
    return res
print(findFloorEl([1,2,3,4,8,10,10,12,19],0))



    
