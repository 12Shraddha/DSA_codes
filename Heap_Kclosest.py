import heapq
def func(arr,x,k):
    s=[]
    heapq.heapify(s)
    for i in range(len(arr)):
        heapq.heappush(s,(abs(arr[i]-x),arr[i]))
        heapq._heapify_max(s)
        if len(s)>k:
            print(s,"before")
            if (abs(arr[i]-x))<=s[0][0]:
                heapq.heappop(s)
                print("after",s)
    return s
            
    pass

print(func([5,6,7,8,9],7,3))