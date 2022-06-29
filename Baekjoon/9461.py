# 9461 파도반 수열

def triangle(n):
    dp=[0]*(n+1)
    # dp[1]=1
    # dp[2]=1
    # dp[3]=1

    if n<=3:
        for i in range(1,n+1):
            dp[i]=1
        return dp[n]
    else:
        dp[1]=1
        dp[2]=1
        dp[3]=1
        for i in range(4, n+1):
            dp[i]=dp[i-2]+dp[i-3]
        return dp[n]
t=int(input())
for _ in range(t):
    n=int(input())
    print(triangle(n))
