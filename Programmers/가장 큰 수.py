def solution(numbers):
    # 사전식 정렬을 위해 문자열 변환
    new_numbers=[str(x) for x in numbers]

    # new_numbers=[]
    # for i in numbers:
    #     new_numbers.append(str(i))
    
    # 사전식 정렬
    new_numbers.sort(key=lambda x:x*3, reverse=True)

    # 리스트 요소를 하나의 문자열로 합치기
    return str(int(''.join(new_numbers)))
