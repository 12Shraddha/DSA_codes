# Brute 
# l=[1,2,3,4,9,6,5,11]
# n=len(l)
# k=3
# total=-1000
# for i in range(n-k+1):
#     total=max(total,sum(l[i:i+k]))
#     print((l[i:i+k]))
# print(total)

#sliding window

def func(l,k):
    n=len(l)
    i=0
    j=0
    total=0
    max1=-1000
    while(j<n):
        total+=l[j]
        if (j-i+1)<k:
            pass    
        elif (j-i+1)==k:
            max1=max(max1,total)
            total-=l[i]
            print(l[i],l[j])
            i+=1
        j+=1
        
    return max1


    pass

print(func([1,2,3,4,9,6,5,11,1],3))


    

                
                
                