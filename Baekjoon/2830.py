# 2830 : 행성X3 : 조합을 문제를 풀었으나, 답은 맞지만 메모리 초과문제가 있음

# import sys
# from itertools import combinations
# input=sys.stdin.readline

# n=int(input()) # 거주민수
# person=[]
# sum=0 # 모든 친밀도의 합

# for _ in range(n):
#     name=person.append(int(input().strip()))

# # 조합
# combi=list(combinations(person,2))

# for i,j in combi:
#     sum+=i^j
# print(sum)

# 맞는 코드
n = int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

onecnt = [0] * 20  # 각 자리수에 따른 1의 개수 count

# 1의 개수 구하기
for i in nums:
    location=0 # 각 자리수
    tmp=i
    while tmp>0:
        onecnt[location]+=tmp%2
        tmp=tmp//2
        location+=1

# 1의 개수와 0의 개수를 곱하고, 2^location 곱한다.
friendly=0 #친밀도
double=1
for i in range(len(onecnt)):
    friendly+=double*onecnt[i]*(n-onecnt[i])
    double=double*2

print(friendly)
