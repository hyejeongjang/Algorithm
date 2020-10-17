def solution(s):
    answer = ''
    s_low=[]
    s_up=[]
    for i in s:
        if(i.islower()):
            s_low.append(i)
        else:
            s_up.append(i)
    s_low.sort()
    s_up.sort()
    s_low.reverse()
    s_up.reverse()
    answer=s_low+s_up
    answer="".join(answer)
    return answer
