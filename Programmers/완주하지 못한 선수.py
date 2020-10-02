def solution(participant, completion):
    answer = ''
    for i in completion:
        for j in range(len(participant)):
            if i==participant[j]:
                participant.pop(j)
                break
    answer=participant[0]
    return answer
