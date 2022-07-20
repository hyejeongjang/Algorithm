# 2953 나는 요리사다

participants=[]
for _ in range(5):
    participants.append(list(map(int, input().split())))

total=[]
for i in range(5):
    score=0
    for j in range(4):
        score=score+participants[i][j]
    total.append(score)

print(total.index(max(total))+1, max(total))
