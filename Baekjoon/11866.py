from collections import deque

answer=[] # 순열 저장할 리스트

n,k=map(int, input().split())
if n==1:
    print("<1>")
    exit()
q=deque()
for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())

print("<", end='')
print(answer[0], end='')
print(",", end='')
print(" ", end='')
for i in range(1, len(answer)):
    if i==len(answer)-1:
        print(answer[i], end='')
        print(">")
    else:
        print(answer[i], end='')
        print(",", end='')
        print(" ", end='')
