def solve(n,one,zero,num):
    if n==0:
        print(num)
        return 
    if one==zero:
        one+=1
        num+="1"
        n-=1
        solve(n,one,zero,num)
    else:
        solve(n-1,one+1,zero,num+"1") or solve(n-1,one,zero+1,num+"0")


def func(n):
    one=0
    zero=0
    num=""
    return solve(n,one,zero,num)

func(3)