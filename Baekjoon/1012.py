from collections import deque

t=int(input())
directions=[(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]=0 # 방문처리
    while q:
        x, y=q.popleft()
        for dx, dy in directions:
            px=x+dx
            py=y+dy
            if px>=m or py>=n or px<0 or py<0:
                continue
            if graph[px][py]==1:
                graph[px][py]=0 # 방문처리
                q.append((px, py))



for _ in range(t): # 테스트 케이스 만큼 for문 반복
    m, n, k=map(int, input().split())
    graph=[[0]*n for _ in range(m)]
    for _ in range(k): # 배추의 개수만큼 반복해서 dfs 실행한다.
        x,y=map(int, input().split())
        graph[x][y]=1
    
    worm=0 # 지렁이 개수 초기화
    for i in range(m):
        for j in range(n):
            if graph[i][j]==1:
                bfs(i,j)
                worm+=1
    print(worm)
