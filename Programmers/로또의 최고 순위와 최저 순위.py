def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    if(lottos==win_nums):
        answer=[1,1]
    elif lottos.count(0)==6:
        answer=[1,6]
    elif len(set(lottos) & set(win_nums))==0 and lottos.count(0)==0: 
        answer=[6,6]
    else:
        both=len(set(lottos) & set(win_nums)) # 교집합
        count_zero=int(lottos.count(0))
        answer.append(7-both-count_zero) # 
        answer.append(7-both)
    return answer

