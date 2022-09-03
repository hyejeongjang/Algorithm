# 14425 문자열 집합

import sys
input=sys.stdin.readline

n,m=map(int, input().split())
s=[]
for _ in range(n):
    s.append(input().strip())
s.sort()
s=set(s)

examine=[]
for _ in range(m):
    examine.append(input().strip())

answer=0
for i in examine:
    if i in s:
        answer+=1
    else:
        pass

print(answer)
