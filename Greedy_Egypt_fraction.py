import math
def solve(n,m,l=[]):
    if n==0:
        return l  
    g=math.ceil((m/n))
    l.append(f'{1}/{g}+')
    print(g)
    return solve((n*g-m),m*g,l)

print(solve(12,13))

