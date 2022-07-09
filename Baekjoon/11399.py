# 11399 ATM

n=int(input())
out_time=list(map(int, input().split()))

total_time=0
out_time.sort()

if n==1:
    print(out_time[0])
else:
    for i in range(1, n):
        out_time[i]+=out_time[i-1]
    print(sum(out_time))
