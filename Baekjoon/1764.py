# 1764 듣보잡
import sys
input=sys.stdin.readline

n,m=map(int, input().split())

listen=[]
for _ in range(n):
    listen.append(input().strip())
listen=set(listen)

see=[]
for _ in range(m):
    see.append(input().strip())
see=set(see)

answer=list(sorted(listen&see))
print(len(answer))
for i in answer:
    print(i)
