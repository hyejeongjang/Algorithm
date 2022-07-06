# 2156 포도주 시식
 
n=int(input())
grape=[0] # 포도주잔
for _ in range(n):
    grape.append(int(input()))

if n==1:
    print(grape[n])
elif n==2:
    print(grape[1]+grape[2])
else:
    dp=[0]*(n+1)
    dp[1]=grape[1]
    dp[2]=grape[1]+grape[2]
    for i in range(3,n+1):
        dp[i]=max(grape[i]+grape[i-1]+dp[i-3], grape[i]+dp[i-2], dp[i-1])
    print(dp[n])
