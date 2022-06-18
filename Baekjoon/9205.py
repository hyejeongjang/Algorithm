from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        dx,dy=q.popleft()
        if abs(dx-rockx)+abs(dy-rocky)<=1000:
            print("happy")
            return
        for i in range(convi_num):
            if visited[i]==0:
                convx, convy=convi[i]
                if abs(dx-convx)+abs(dy-convy)<=1000:
                    q.append((convx, convy))
                    visited[i]=1
    print("sad")                


t=int(input())
for _ in range(t):
    convi_num=int(input()) # 편의점 개수
    homex, homey=map(int, input().split())
    convi=[]
    for _ in range(convi_num):
        convix, conviy=map(int, input().split())
        convi.append((convix, conviy))
    # 편의점 탐색 여부 확인하기 위한 리스트
    visited=[0 for _ in range(convi_num)]
    rockx, rocky=map(int, input().split())
    bfs(homex, homey) #처음 집(시작점)부터 bfs로 전달 수 편의점 개수만큼 탐색 후 락페 종점까지 가본다.
