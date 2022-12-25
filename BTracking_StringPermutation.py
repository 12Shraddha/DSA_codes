def func(s,l,r,op=""):
    if l==r-1:
        print("".join(s))
        return
    for i in range(l,r):
        s[l],s[i]=s[i],s[l]
        func(s,l+1,r,op)
        s[l],s[i]=s[i],s[l]

(func(list("ABc"),0,3))

