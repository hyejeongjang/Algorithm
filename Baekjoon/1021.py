# 1021 : 회전하는 큐
from collections import deque

n,m=map(int, input().split())
nums=[i+1 for i in range(n)]
nums=deque(nums)

pops=list(map(int, input().split()))

ans=0

for i in pops:
    while i in pops:
        if i==nums[0]:
            nums.popleft()
            break
        else:
            if nums.index(i)<=len(nums)//2:
                # 2번 실행 : 왼쪽이동
                nums.rotate(-1)
                ans+=1
            else:
                nums.rotate(1)
                ans+=1
print(ans)
