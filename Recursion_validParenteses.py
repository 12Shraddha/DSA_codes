def func(open,close,c):
    if open==close and open!=0:
        open-=1
        c+="("
    if open==0 and close==0 :
            print(c)
            return
    # print("OPEN:",open," CLOSE: ",close,c)
    if open==0:
        func(open,close-1,c+")") 
    elif open<close:
        func(open,close-1,c+")")
        func(open-1,close,c+"(") 

def solve(n):
    c=""
    open=n
    close=n
    return func(open,close,c)
    
         
solve(3)
    


