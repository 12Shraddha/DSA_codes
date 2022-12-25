s="banana"
r="ana"


n=len(s)
m=len(r)

count=0
nump,temp=0,0
for i in range(m):
    nump=nump*10+ord(s[i])
    temp=temp*10+ord(r[i])
if temp==nump:
    count+=1
print(temp,nump)
for i in range(1,n-m+1):
    nump=nump-ord(s[i-1])*(10**(m-1))
    nump=nump*(10)+ord(s[i+m-1])
    print(nump)
    if nump==temp:
        count+=1
print(count)