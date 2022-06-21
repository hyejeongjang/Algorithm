# 7569 토마토

from collections import deque

directions=[(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

m,n,h=map(int, input().split())
graph=[[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))

q=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                q.append((i, j, k))

days=0 # 날짜(리턴값)
while q:
    days+=1
    for _ in range(len(q)):
        z, y, x=q.popleft()
        for dz, dy, dx in directions:
            pz=dz+z
            py=dy+y
            px=dx+x
            if pz>=h or py>=n or px>=m or pz<0 or py<0 or px<0:
                continue
            if graph[pz][py][px]==0:
                graph[pz][py][px]=1
                q.append((pz, py, px))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==0:
                print(-1)
                exit()

print(days-1)
