import operator

def solution(N, stages):
    answer=[] # 스테이지의 번호를 실패율의 내림차순으로 정리
    failure={} # 스테이지 번호(key), 실패율(value) 딕셔너리
    
    user=len(stages) # 총 도전한 사용자 수
    for i in range(1, N+1):
        if user==0:
            failure[i]=0
        else:
            not_in_stage=stages.count(i) # 클리어 하지 못한 사용자 수
            failure[i]=not_in_stage/user
        user=user-not_in_stage # 다음 스테이지에서 도전할 사용자의 수를 계산 하기 위해 먼저 해당 스테이지에서 클리어한 수를 제한다.
        
    return sorted(failure, key=lambda x:failure[x], reverse=True)
