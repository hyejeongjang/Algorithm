# 1946 신입 사원

import sys
t=int(input())

for _ in range(t):
    people=[]
    n=int(input()) # 지원자수
    for i in range(n):
        s,m=map(int, sys.stdin.readline().split()) # 서류성적,면접성적
        people.append([s,m])

    people.sort()
    max=people[0][1]
    number=1 # 최고득점자는 자동으로 선발
    for i in range(1, n):
        if max>people[i][1]:
            number+=1
            max=people[i][1]
    print(number)
