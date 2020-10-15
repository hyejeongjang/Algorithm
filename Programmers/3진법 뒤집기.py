def solution(n):
    answer = 0
    q_list=[]
    while n>0:
        n,q=divmod(n,3)
        q_list.append(q)
    q_list.reverse()
    for i in range(len(q_list)-1, -1, -1):
        answer=answer+q_list[i]*3**i
    return answer
