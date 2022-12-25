def nextAlphabet(l,s):
    left=0
    n=len(l)
    right=n-1
    nex_=1000
    while(left<=right):
        mid=int(left+(right-left)/2)
        if l[mid]==s :
            if mid+1<=n-1:
                return l[mid+1]
            else:
                return -1
        elif l[mid]>s:
            nex_=l[mid]
            right=mid-1
        else:
            left=mid+1
    return (nex_)

print(nextAlphabet(["a","c","f","h"],"d"))