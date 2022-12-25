import heapq
def func(arr,k):
    s=[]
    heapq.heapify(s)
    for i in range(len(arr)):
        heapq.heappush(s,arr[i])
        if len(s)>k:
            arr[i-k]=s[0]
            s[-1],s[0]=s[0],s[-1]
            print(arr)
            heapq.heapify(s)
            heapq.heappop(s)
    for i in range(1,k+1):
        arr[-i]=s[-i]
    
    return arr

print(func([1,5,3,2,8,10,9],k=3))