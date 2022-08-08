# 10816 숫자 카드 2

n=int(input())
cards=list(map(int, input().split()))

m=int(input())
numbers=list(map(int, input().split()))

answer={}
# m의 숫자들을 딕셔러리의 키로, 몇개가 있는지 value로 저장

for i in cards:
    if i in answer:
        answer[i]+=1
    else:
        answer[i]=1

for i in numbers:
    if i in answer:
        print(answer[i], end=' ')
    else:
        print(0, end=' ')
