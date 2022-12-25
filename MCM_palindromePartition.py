def isPalindrome(s):
    x=s[::-1]
    if s==x:
        return True
    return False


def func(s,i,j):
    if i>=j or isPalindrome(s[i:j+1]):
        return 0
    mn=1000
    for k in range(i,j):
        count=(func(s,i,k)+1+func(s,k+1,j))
        mn=min(mn,count)
    return mn
print(func("aabc",0,3))


    


