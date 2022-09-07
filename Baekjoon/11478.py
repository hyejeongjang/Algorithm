# 11478 서로 다른 부분 문자열의 개수

import sys
input=sys.stdin.readline

word=input().strip()
w=len(word)
answer=[]

if w==1:
    print(1)
else:
    for i in range(w):
        if i==0:
            for j in word:
                answer.append(j)
        else:
            loops=w-i
            i=i+1
            cnt=0
            for j in range(loops):
                answer.append(word[cnt:cnt+i])
                cnt+=1
                if j==loops-1:
                    cnt=0
print(len(set(answer)))
