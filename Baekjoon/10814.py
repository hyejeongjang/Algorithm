# 10814 나이순 정렬

import sys
input=sys.stdin.readline

n=int(input())
member=[]
for i in range(n):
    a,b=map(str, input().split())
    member.append([i,int(a),b])

# 정렬
member.sort(key=lambda x:(x[1], x[0]))

for i in range(n):
    print(member[i][1], member[i][2])
