# 11725 트리의 부모 찾기

from collections import deque
import sys

# 노드의 개수
n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
parent=[0 for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

q=deque()
q.append(1)

while q:
    x=q.popleft()
    for i in graph[x]:
        if parent[i]==0:
            parent[i]=x
            q.append(i)

for i in parent[2:]:
    print(i)
