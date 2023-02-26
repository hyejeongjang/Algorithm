def solution(s):
    s=list(s)
    sstack=[]
    sstack.append(s.pop(0))
    
    for i in s:
        if i=="(":
            sstack.append(i)
        else:
            if sstack:
                sstack.pop()
            else:
                return False
            
    if len(sstack)>0:
        return False
    else:
        return True
