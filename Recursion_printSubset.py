#CHOICE DIAGRAM
def subset(s,n,c=""):
    if n==0:
        print(c)  
        return 
    
    subset(s,n-1,s[n-1]+c) or subset(s,n-1,c)
(subset("ab",3))

##IP/OP
def ipop(ip,op=""):
    if ip=="":
        print(op)
        return
    # print(ip)
    op1=op
    op2=op
    t=ip[0]
    op2+=t
    ip=ip[1:]
    # print(t,ip,op1,op2)
    ipop(ip,op1) or ipop(ip,op2)
    return 
ipop("abc")



