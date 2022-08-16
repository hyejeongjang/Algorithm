# 17070 파이프 옮기기 1

from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))
count=0

def dfs(x,y,directions):
    global count
    if x==n-1 and y==n-1:
        count+=1
        return
        # 가로
    if directions==0:
        if y+1<n and graph[x][y+1]==0:
            dfs(x,y+1,0)
        if x+1<n and y+1<n:
            if graph[x+1][y+1]==0 and graph[x][y+1]==0 and graph[x+1][y]==0:
                dfs(x+1,y+1,2)
    # 세로
    elif directions==1:
        if x+1<n and graph[x+1][y]==0:
            dfs(x+1,y,1)
        if x+1<n and y+1<n:
            if graph[x+1][y+1]==0 and graph[x][y+1]==0 and graph[x+1][y]==0:
                dfs(x+1, y+1, 2)
    # 대각선
    elif directions==2:
        if x+1<n and graph[x+1][y]==0:
            dfs(x+1, y, 1)
        if y+1<n and graph[x][y+1]==0:
            dfs(x, y+1,0)
        if x+1<n and y+1<n:
            if graph[x][y+1]==0 and graph[x+1][y+1]==0 and graph[x+1][y]==0:
                dfs(x+1, y+1, 2)

dfs(0,1,0)
print(count)
