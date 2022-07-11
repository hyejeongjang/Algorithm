# 1427 소트인사이드

n=list(input())
answer=""
n.sort()
for i in n:
    answer=i+answer
print(answer)
