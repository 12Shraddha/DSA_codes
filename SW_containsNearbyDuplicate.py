def containsNearbyDuplicate(l, k):  
    n=len(l)
    i,j=0,0
    d=[]
    while(j<n):
        d.append(l[j])
        if (j-i)<k:
            pass
        elif (j-i)==k:
            for m in d:
                if d.count(m)>1:
                    return("true")         
            d.remove(l[i])
            i+=1
        j+=1
    return ('false')
print(containsNearbyDuplicate([1,2,3,1,2,3],3))