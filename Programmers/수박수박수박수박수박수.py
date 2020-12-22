def solution(n):
    catch1="수박"
    catch2="수"
    answer = '' # 초기화
    num1=n//2 # 수박 몇번 반복
    num2=n%2 # 수가 붙을지 말지
    answer=catch1*num1+catch2*num2
    return answer
