def solution(a, b):
    answer = 0
    big=0 # max값
    small=0 # min값
    if(a>b):
        big=a
        small=b
    else:
        small=a
        big=b
    for i in range(small, big+1):
        answer=answer+i
    return answer
