def solution(numbers, direction):
    answer=[]
    if direction=="right":
        answer.append(numbers.pop())
        for i in numbers:
            answer.append(i)
    else:
        tmp=numbers.pop(0)
        for i in numbers:
            answer.append(i)
        answer.append(tmp)
    return answer
