def solution(s):
    s=list(s)
    answer = ''
    if(len(s)%2==0):
        ans=len(s)//2
        answer=answer+s[ans-1]+s[ans]
    else:
        ans=len(s)//2
        answer=answer+s[ans]
    return answer
