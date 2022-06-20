from collections import deque

directions=[(1,0), (-1,0), (0,1), (0,-1)]
big_paint=[0] # 그림의 넓이 저장 리스트

def bfs(y,x):
    q=deque()
    q.append((y,x))
    graph[y][x]=0
    volume=0
    while q:
        y,x=q.popleft()
        volume+=1
        for dy, dx in directions:
            py=y+dy
            px=x+dx
            if py>=n or px>=m or py<0 or px<0:
                continue
            if graph[py][px]==1:
                q.append((py, px))
                graph[py][px]=0 # 방문처리
                #volume+=1
                
    big_paint.append(volume)


n,m=map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

paint_num=0 # 그림의 개수
for i in range(n):
    for j in range(m):
        # j가 x, i가 y
        if graph[i][j]==1:
            bfs(i,j)
            paint_num+=1
            graph[i][j]==0 # 방문처리

print(paint_num) # 그림의 개수
print(max(big_paint)) # 그림의 넓이의 최대값
