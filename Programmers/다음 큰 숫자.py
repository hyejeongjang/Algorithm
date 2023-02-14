def solution(n):
    answer = 0
    two_n=format(n, 'b')
    count_one=str(two_n).count('1')
    print(count_one)
    while True:
        n+=1
        two_n=format(n,'b')
        if str(two_n).count('1')==count_one:
            answer=n
            break
    return answer
