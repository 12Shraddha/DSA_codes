#COUNT O(n^2)
# def func(arr):
#     n=len(arr)
#     s=[-1]
#     count=0
#     res=[1 for i in range(n)]
#     for i in range(n):
#         for j in range(i,-1,-1):
#             if s[j]<=arr[i]:
#                 count+=1
    
#         res[i]=count
#         count=0
#         s.append(arr[i])
    
#     return res
# print(func([3,0,0,1,2,4]))

#INDEX

def func(arr):
    n=len(arr)
    s=[-1]
    res=[i for i in range(n)]
    for i in range(n):
        j=i
        while(j>0):
            if s[j]<=arr[i]:
                j-=1
            else:
                res[i]=j
                break
        if j==0:
            res[i]=0        
        s.append(arr[i])
    
    return res
print(func([6,2,5,4,5,1,6]))