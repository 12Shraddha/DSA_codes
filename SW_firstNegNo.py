#1
def func(arr,k):
    n=len(arr)
    store=[]
    res=[0]*(n-k+1)
    i,j=0,0
    while (j<n):
        if arr[j]<0:
            store.append(arr[j])
        if j-i+1==k:
            if len(store)!=0:
                res[i]=store[0]
                if store[0]==arr[i]:
                    store.pop(0)
            i+=1
    

        j+=1
    return res
print(func([-1,3,4,-2,-3,0,9,8],3))

# #2
# def func(arr,k):
#     n=len(arr)
#     stores=[]
#     res=[0]*(n-k+1)
#     for i in range(k):
#         stores.append(arr[i])
#         if arr[i]<0 and res[0]==0:
#             res[0]=arr[i]
#     j=1
#     for i in range(k,n):
#         stores.append(arr[i])
#         stores.pop(0)
#         for store in stores:
#             if res[j]==0 and store<0:
#                 res[j]=store
#         j+=1
#     return res
# print(func([-1,3,4,-2,-3,0,9,8],3))

# #brute

# l=[0,-1,-9,8,7,-6]
# k=3
# n=len(l)
# for i in range(n-k+1):
#     flag=True
#     for j in range(i,i+k):
#         if l[j]<0:
#             flag=False
#             print(l[j])
#             break
#     if flag:
#         print("Not there")
    


