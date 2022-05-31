def solution(no, works):
    answer=0
    #  배상할 비용이 없을 때
    if no>=sum(works):
        return 0
    for i in range(no):
        works=sorted(works)
        works[-1]=works[-1]-1
    answer=sum([i**2 for i in works])
    
    return answer
