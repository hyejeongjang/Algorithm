# 1697 숨바꼭질

from collections import deque

# n: 수빈, k: 동생
n,k=map(int, input().split())
max_point=100000
visited=[0]*(max_point+1)

q=deque()
q.append(n)
while q:
    x=q.popleft()
    if x==k:
        print(visited[x])
        break
    for i in (x-1, x+1, x*2):
        if 0<=i<=100000 and not visited[i]:
            visited[i]=visited[x]+1
            q.append(i)
