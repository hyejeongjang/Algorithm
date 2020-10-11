def solution(arr, divisor):
    answer = []
    count=0
    for i in arr:
        if(i%divisor==0):
            answer.append(i)
        else:
            count=count+1
    if(count==len(arr)):
        answer.append(-1)
    answer.sort()
    return answer
