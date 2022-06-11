from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))
    
directions=[(0,1), (0,-1), (1,0), (-1,0)]

queue=deque()
queue.append((0,0))
while queue:
    y, x=queue.popleft()
    for dy,dx in directions:
        py=y+dy
        px=x+dx


        if px >=m or py >=n or px <0 or py<0:
            continue
        
        # 만약 1이여서 방문이 가능하다면, 방문 후 1을 더해준다.
        if maze[py][px]==1:
            # maze[py][px]+=maze[x][y]
            maze[py][px]=maze[y][x]+1
            queue.append((py, px))

print(maze[n-1][m-1])
