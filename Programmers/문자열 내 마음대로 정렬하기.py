def solution(strings, n):
    answer = []
    new=[]
    for i in strings:
        new.append(i[n]+i[0:n]+i[n+1:])
    new.sort()
    for j in new:
        answer.append(j[1:n+1]+j[0]+j[n+1:])
    return answer
