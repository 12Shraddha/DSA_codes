def solve(s,k):
    print(k)
    if k==1:
        s.pop()
        return s
    temp=s[-1]
    s.pop()
    solve(s,k-1)
    s.append(temp)
    return s

def delete(s,n):
    k=n//2
    if len(s)==0:
        return s
    return solve(s,k)

print(delete([1,2,3,4,5,4],6))
    



