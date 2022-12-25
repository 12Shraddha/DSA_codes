def func(s,k):
    n=len(s)
    i,j=0,0
    mx=0
    d={}
    while(j<n):
        if s[j] not in d:
            d[s[j]]=1
        else:
            d[s[j]]+=1
   
        if len(d)==k:
            mx=max(mx,j-i+1)
        elif len(d)>k:
            while(len(d)>k):
                d[s[i]]-=1
                i+=1
                print(d)
                for l,m in d.items():
                    if m==0:
                        del d[l]
                        break

        j+=1
    return mx

print(func("aabacbebebe",3))
                
            
            
            

