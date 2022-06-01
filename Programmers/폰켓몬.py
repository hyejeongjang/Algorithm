def solution(nums):
    answer = 0
    # 골라야 하는 폰켓몬 수
    ponketmon=len(nums)/2
    
    # 중복 제거
    set_num=set(nums)
    nums=list(set_num)
    
    if ponketmon>len(nums):
        answer=len(nums)
    else:
        answer=ponketmon
    return answer
