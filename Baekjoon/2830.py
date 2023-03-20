# 2830 : 행성 X3
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
