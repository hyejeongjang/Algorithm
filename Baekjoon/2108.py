# 2108 통계학

import sys
input=sys.stdin.readline
from collections import Counter

n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

# 산술평균(소수점 첫째자리에서 반올림)
print(round(sum(nums)/n))

# 중앙값
nums.sort()
print(nums[n//2])

# 최빈값
cnt=Counter(nums).most_common()
if len(cnt)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
# 범위
print(nums[-1]-nums[0])
