def reverse(s,v):
    if len(s)==0:
        return s.append(v)
    else:
        tmp=s.pop()
        reverse(s,v)
        s.append(tmp)
        return s

    pass
def func(s):
    if len(s)==1:
        return s
    else:
        v=s.pop()
        print(v,s)
        func(s)
        reverse(s,v)
        return s
print(func([1,2,3,4,5]))



