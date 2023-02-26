def solution(clothes):
    answer = 1
    dic_clothes={}
    for i in clothes:
        if i[1] in dic_clothes:
            dic_clothes[i[1]]+=1
        else:
            dic_clothes[i[1]]=1
            
    print(dic_clothes)
    ans=list(dic_clothes.values())
    
    for i in ans:
        answer=answer*(i+1)
    print(answer)
    # 의상의 종류를 모두 곱한 후에 아무것도 입지 않은 경우의 수 1을 빼준다.
    return answer-1
