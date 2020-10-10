def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr)):
        if(i==0):
            continue
        if (arr[i-1]!=arr[i]):
            answer.append(arr[i])
    return answer
