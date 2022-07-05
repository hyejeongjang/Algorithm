# 16928 뱀과 사다리 게임

from collections import deque

def bfs(n):
    q=deque()
    q.append(n)
    visited[n]=1 # 방문처리

    while q:
        x=q.popleft()
    
        for i in range(1,7):
            dx=x+i #dice x
        
            if dx>100:
                continue

            now=graph[dx]
        
            if visited[now]==0:
                q.append(now)
                visited[now]=visited[x]+1

                if now==100:
                    return
                    
# n : 사다리 정보, m : 뱀의 정보
n,m=map(int, input().split())

graph=[i for i in range(101)]
for _ in range(n+m):
    a,b=map(int, input().split())
    graph[a]=b

# 던진 횟수
visited=[0]*101
bfs(1)

print(visited[100])
