from collections import deque

n=int(input())
directions=[(1,0), (-1,0), (0,1), (0,-1)]

graph=[]
graph_max=0

def bfs(x,y, target):
    q=deque()
    q.append((x,y))
    visited[x][y]=1 # 방문처리
    while q:
        x,y=q.popleft()
        for dx, dy in directions:
            px=dx+x
            py=dy+y
            if px>=n or py>=n or px<0 or py<0:
                continue
            if graph[px][py]>target and visited[px][py]==0:
                visited[px][py]=1
                q.append((px, py))

for j in range(n):
    graph.append(list(map(int, input().split())))

# 그래프의 최대값 찾기
graph_max=max(map(max, graph))

result=[]
for i in range(graph_max+1):
    visited=[[0]*n for i in range(n)] # 방문여부 확인
    now=0
    for j in range(n):
        for k in range(n):
            if graph[j][k]>i and visited[j][k]==0:
                bfs(j, k, i) # i는 높이
                now+=1
    result.append(now)

print(max(result))
