# 24416 알고리즘 수업 - 피보나치 수 1

# 재귀
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# 동적 프로그래밍
def dp_fib(n):
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=1
    cnt=0
    for i in range(3, n+1):
        cnt+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt

n=int(input())
print(fib(n), dp_fib(n))
