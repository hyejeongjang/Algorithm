from collections import deque

n=int(input())
town=[]
for i in range(n):
  town.append(list(map(int, input())))

directions=[(1,0), (-1,0), (0,1), (0,-1)]

houses=[]

total=0 # 총 단지수
def bfs(y,x):
    count=1
    q=deque()
    q.append((y, x))
    town[y][x]=0
    while q:
        y,x=q.popleft()
        for dy, dx in directions:
            py=y+dy
            px=x+dx
            if px>=n or py>=n or px<0 or py<0:
                continue
            if town[py][px]==1:
                town[py][px]=0
                q.append((py, px))
                count+=1
    houses.append(count)

for i in range(n):
    for j in range(n):
        if town[i][j]==1:
            bfs(i, j)
            total+=1 # 총 단지수

houses.sort()

print(total)
for i in houses:
    print(i)
