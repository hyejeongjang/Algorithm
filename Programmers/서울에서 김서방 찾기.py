def solution(seoul):
    answer = ''
    number=0
    if "Kim" in seoul:
        number=seoul.index("Kim")
    answer="김서방은 "+str(number)+"에 있다"
    return answer
