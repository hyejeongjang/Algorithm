# 2606 바이러스

from collections import deque

computer=int(input())
n=int(input())
graph=[[]*(computer+1) for i in range(computer+1)]
visited=[False]*(computer+1)
# print(graph)

for _ in range(n):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, v):
    # 큐 설정 먼저 하기
    q=deque()
    q.append(v)
    cnt=0

    # q에 원소가 있을 동안 반복
    while q:
        # q에서 원소 빼오기
        x=q.popleft()
        visited[x]=True

        for i in graph[x]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
                cnt+=1

    return cnt

print(bfs(graph,1))
