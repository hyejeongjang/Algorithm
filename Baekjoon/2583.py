# 2583 영역 구하기
from collections import deque
directions=[(1,0), (-1,0), (0,1), (0,-1)]

def bfs(a,b):
    q=deque()
    q.append((a,b))
    count=1
    while q:
        y,x=q.popleft()
        for dy,dx in directions:
            sy=y+dy
            sx=x+dx
            if sy>=m or sx>=n or sy<0 or sx<0:
                continue
            if graph[sy][sx]==0:
                graph[sy][sx]=1
                q.append((sy, sx))
                count+=1
    return count

# m*n,(y,x), k개
m,n,k=map(int, input().split())
graph=[[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2=map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1

area=[]

for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j]=1
            area.append(bfs(i,j))
print(len(area))
print(*sorted(area))
