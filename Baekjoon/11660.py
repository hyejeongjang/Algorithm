# 11660 : 구간 합 구하기 2

import sys
input=sys.stdin.readline

n,m=map(int, input().split())

nums=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    nums.append(tmp)

# 구간 합 구하기 : 맨 처음 nums를 만들 때에는 n개로 만들었기 때문에
# 문제에서 1부터라고 한 조건에 맞지 않는다. nums는 (1,1)을 (0,0)으로 생각하기 때문에
# sums에서는 n+1로 배열을 만들기 때문에 (1,1)을 그대로 (1,1)로 받아들일 수 있다.
# 그래서 sums를 구하는 마지막 nums에서는 nums(i,j)==nums[i-1][j-1]
# 배열의 크기를 일치시키지 않아 문제가 발생했었다.

sums=[]
for _ in range(n+1):
    sums.append([0]*(n+1))

for i in range(1,n+1):
    for j in range(1, n+1):
        sums[i][j]=sums[i][j-1]+sums[i-1][j]-sums[i-1][j-1]+nums[i-1][j-1]

# 답 출력
for _ in range(m):
    x1,y1,x2,y2=map(int, input().split())
    ans=sums[x2][y2]-sums[x1-1][y2]-sums[x2][y1-1]+sums[x1-1][y1-1]
    print(ans)
