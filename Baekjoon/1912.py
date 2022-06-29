# 1912 연속합

n=int(input())
num_list=list(map(int, input().split()))

dp=[0]*n
dp[0]=num_list[0]

for i in range(1,n):
    dp[i]=max(num_list[i], num_list[i]+dp[i-1])
print(max(dp))
