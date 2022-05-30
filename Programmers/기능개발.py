import math 
def solution(progresses, speeds):
    answer=[] # 각 배포마다 몇 개의 기능이 배포되는지
    days=[] # 각 기능별 소요 시간
    # 각 기능별 남은 진도

    for idx, val in enumerate(progresses):
        days.append(math.ceil((100-val)/speeds[idx]))
        
    max_days=days[0]
    count=0
    for idx, val in enumerate(days):
        if max_days<val:
            answer.append(count)
            count=0
            max_days=val
        count+=1
            
    if count>0:
        answer.append(count)
    return answer
