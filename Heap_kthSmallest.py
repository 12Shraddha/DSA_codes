import heapq 
def func(arr,k,n):
    stack=[]
    for i in range(k):
        heapq.heappush(stack,arr[i])
        heapq._heapify_max(stack)
    
    for i in range(k,n):
        if arr[i]< stack[0]:
            stack[0]=arr[i]
            heapq._heapify_max(stack)
    return stack[0]

print(func([7,4,3,9,10,1],3,6))

        