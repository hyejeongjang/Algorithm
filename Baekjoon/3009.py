# 3009 네 번째 점

square_x=[]
square_y=[]

for _ in range(3):
    a,b=map(int, input().split())
    square_x.append(a)
    square_y.append(b)

answer=[]

for i in square_x:
    cnt=square_x.count(i)
    if cnt==1:
        answer.append(i)
        break

for j in square_y:
    cnt=square_y.count(j)
    if cnt==1:
        answer.append(j)
        break

print(*answer)
