def solution(brown, yellow):
    total = brown + yellow
    
    for width in range(1, total):
        if total%width==0:
            vertical=total//width # 세로는 전체에서 가로를 나눈 몫
            if (width-2)*(vertical-2)==yellow:
                return [vertical, width]
