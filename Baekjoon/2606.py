# 2606 바이러스
from collections import deque

computer=int(input())
network=int(input())
graph=[[0]*(computer+1) for _ in range(computer+1)]
for _ in range(network):
    a,b=map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

infection=0 # 감염된 컴퓨터 수
visited=[0]*(computer+1)
count=0

q=deque()
q.append(1)

while q:
    x=q.popleft()
    visited[x]=1
    
    for i in range(1, computer+1):
        if graph[x][i]==1 and visited[i]==0:
            visited[i]=1
            q.append(i)
            count+=1

print(count)

