def insert(l,v):
    n=len(l)
    if n==0 or  l[n-1]<=v:
        return l.append(v)
       
    elif l[0]>=v:
        return l.insert(0,v)
    else:
        val=l[n-1]
        l.pop()
        print("v in insert ",v, val,l)
        insert(l,v)
        l.append(val)

def sort(l):
    if len(l)==1:
        return l
    v=l[len(l)-1]
    l.pop()
    print("v in sort",v,l)
    sort(l)
    insert(l,v)
    return l

        
l=[2,3,4,1,8,7,5,4]
print(sort(l))
