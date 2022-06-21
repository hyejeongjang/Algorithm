# 7576 토마토

from collections import deque
m,n=map(int, input().split())
graph=[] # 토마토
for _ in range(n):
    graph.append(list(map(int, input().split())))

directions=[(1,0), (-1,0), (0,1), (0,-1)]

# 익은 토마토들(1) 다 큐에 넣는다.
q=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append((i,j))

days=0 # 출력값
while q:
    y,x=q.popleft()
    for dy, dx in directions:
        py=y+dy
        px=x+dx

        if px>=m or py>=n or px<0 or py<0:
            continue
        if graph[py][px]==0:
            graph[py][px]=graph[y][x]+1
            q.append((py, px))

# for i in graph:
#     for j in i:
#         if j==0:
#             print(-1)
#             exit(0)
#     days=max(days, max(i))

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(-1)
            exit()
    days=max(days, max(graph[i]))

print(days-1)
