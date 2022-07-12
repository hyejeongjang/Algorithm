# 1992 쿼드트리

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input())))

def solution(x,y,n):
    color=graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color!=graph[i][j]:
                print("(", end='')
                solution(x,y,n//2)
                solution(x,y+n//2, n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                print(")", end='')
                return
    if color==0:
        print('0', end='')
    else:
        print('1', end='')

solution(0,0,n)
