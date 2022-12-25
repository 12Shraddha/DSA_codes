def insert(arr,k):
    n=len(arr)
    if n==0 or arr[-1]<=k:
        arr.append(k)
        return 
    r=arr.pop()
    insert(arr,k)
    arr.append(r)

def func(arr):
    n=len(arr)
    if n==1:
        return arr
    k=arr.pop()
    func(arr)
    insert(arr,k)
    return (arr)

print(func([1,3,2,-1]))