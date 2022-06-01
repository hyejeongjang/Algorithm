def solution(numbers):
    answer = 0
    non_numbers=[1,2,3,4,5,6,7,8,9]
    numbers=sorted(numbers)
    for i in non_numbers:
        if i not in numbers:
            answer=answer+i
    return answer
