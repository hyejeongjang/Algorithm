# 11650 좌표 정렬하기

import sys
input=sys.stdin.readline

coordinate=[]
n=int(input())
for _ in range(n):
    a,b=map(int, input().split())
    coordinate.append([a,b])

coordinate.sort(key=lambda x : (x[0], x[1]))

# 출력
for i in range(n):
    print(*coordinate[i])
