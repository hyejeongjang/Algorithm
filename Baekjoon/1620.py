# 1620 나는야 포켓몬 마스터 이다솜

import sys
input=sys.stdin.readline

n,m=map(int, input().split())
poket={}
for i in range(n):
    name=input().strip()
    poket[str(i+1)]=name

test=[]
for _ in range(m):
    test.append(input().strip())

reverse_poket={v:k for k,v in poket.items()}

for i in test:
    i=str(i)
    if i in poket:
        print(poket[i])
    elif i in reverse_poket:
        print(reverse_poket[i])
