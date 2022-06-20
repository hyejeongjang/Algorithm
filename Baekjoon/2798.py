# 2798 : 블랙잭
n, m=map(int, input().split())
cards=list(map(int, input().split()))
answer=0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i]+cards[j]+cards[k]>m:
                continue
            else:
                card_sum=cards[i]+cards[j]+cards[k]
                answer=max(answer, card_sum)
             
# # 순열 조합 라이브러리 사용
# from itertools import combinations
# for choose in combinations(cards, 3):
#     tmp_sum=sum(choose)
#     if answer<tmp_sum<=m:
#         answer=tmp_sum

print(answer)
