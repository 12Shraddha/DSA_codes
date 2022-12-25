#count of an element in sorted array
def func(k,l):
    n=len(l)
    left=0
    right=n-1
    count=0
    index_left=0
    index_right=0
    while(left<=right):
        mid=int(left +(right-left)//2)
        if l[mid]==k:
            count+=1
            index_left=mid
            right=mid-1
        elif l[mid]>k:
            right=mid-1
        else:
            left=mid+1
    left=0
    right=n-1
    if count==0 and index_left==0:
        return count,index_left

    while(left<=right):
        mid=int(left +(right-left)/2)
        if l[mid]==k:
            count+=1
            left=mid+1
            index_right=mid
        elif l[mid]>k:
            right=mid-1
        else:
            left=mid+1
    return count-1, index_right-index_left+1

print(func(12,[2,4,10,10,10,12,20]))


