def func(arr):
    n=len(arr)
    s=[]
    for i in arr:
        if i=="(":
            s.append(i)
        elif i==")":
            if s[-1]!="(":
                return ("Invalid")
            else:
                s.pop()

    if len(s)==0:
        return ("Valid")
    return ("Invalid")

print(func("(()())("))

