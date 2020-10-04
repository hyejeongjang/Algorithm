def solution(n, lost, reserve):
    answer = 0
    
    only_lost=list(set(lost)-set(reserve))
    only_reserve=list(set(reserve)-set(lost))
    answer=n-len(only_lost)
    
    for i in only_lost:
        for j in range(len(only_reserve)):
            #if(i==reserve[j]):
                #reserve.pop(j)
                #answer=answer+1
                #break
            if(i-1==only_reserve[j] or i+1==only_reserve[j]):
                only_reserve.pop(j)
                answer=answer+1
                break
    return answer
