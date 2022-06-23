# 7562 나이트의 이동

from collections import deque

directions=[(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]

def bfs(y,x):
    q=deque()
    q.append((y,x))
    # graph[y][x]=1
    while q:
        y,x=q.popleft()
        if y==last_y and x==last_x:
            return
        for dy, dx in directions:
            py=y+dy
            px=x+dx
            if py>=l or px>=l or px<0 or py<0:
                continue
            # 만약 방문하지 않았더라면
            if graph[py][px]==0:
                q.append((py, px))
                graph[py][px]=graph[y][x]+1
        

# 테스트 케이스의 개수
t=int(input())
for _ in range(t):
    l=int(input())
    first_y, first_x=map(int, input().split())
    last_y, last_x=map(int, input().split())

    # 모든 원소가 0인 그래프 만들기
    graph=[]
    for _ in range(l):
        graph.append([0]*l)

    # graph[first_y][first_x]=1
    bfs(first_y, first_x)
    print(graph[last_y][last_x])
