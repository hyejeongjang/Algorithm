from collections import deque

def solution(m, n, infests, vaccinateds):
    directions=[(1,0), (-1,0), (0,1), (0,-1)]
    
    # 방을 만들어주자!
    room =[[False for _ in range(n)] for _ in range(m)]
    
    # 이미 걸린 사람들을 방에 넣자!
    for r,c in infests:
        room[r-1][c-1]=1
    
    # 백신에 맞은 사람들을 방에 넣자!
    for r,c in vaccinateds:
        room[r-1][c-1]=-1
    
    blank=m*n-len(infests)-len(vaccinateds)
    # 만약 처음 모든 직원이 백신을 맞거나 전염병을 앓으면
    if blank==0:
        return 0
    # 병에 모두 감염되기까지 소요되는 시간 계산
    day=0
    
    # dfs, bfs를 위한 큐에 넣기
    q=deque(infests)
    
    # 큐에 원소가 있을 떄 까지
    while q:
        day+=1 # 1일차씩 더해준다
        new_infests=[] # 새롭게 감염된 사람들의 리스트
        y, x=q.popleft()
        x=x-1
        y=y-1
        for _ in range(len(infests)):
            for dy, dx in directions:
                py=y+dy
                px=x+dx
                # if py>=m or px>=n or py<0 or px<0:
                #     continue
                # 만약 백신을 맞지 않은 사람이면
                if -1<=py<m and -1<=px<n and room[py][px] == False:
                    new_infests.append([py, px])
                    # 날짜가 지남에 따라 병에 걸린 사람을 room에 업데이트
                    room[py][px]=1
                    print(room)
                    blank-=1
        q=deque(new_infests)
        print("day",day)
        
    return day if blank ==0 else -1
