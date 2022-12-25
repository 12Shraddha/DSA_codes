def func(ip,op=""):
    if ip=="":
        print(op)
        return 
    op1=op
    op2=op
    t=ip[0]
    ip=ip[1:]
    op1+=t
    op2+=t.swapcase()
    
    func(ip,op1)
    func(ip,op2)

(func("a1B2"))
