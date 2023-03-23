# 11659 : 구간 합 구하기 1

n,m=map(int, input().split())
nums=list(map(int, input().split()))
dp=[0]

tmp=0
for i in nums:
    tmp=tmp+i
    dp.append(tmp)

for _ in range(m):
    a,b=map(int, input().split())
    print(dp[b]-dp[a-1])
