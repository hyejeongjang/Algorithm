# 18870 좌표 압축
import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int, input().split()))

new_nums=list(sorted(set(nums)))

dic={}
for i in range(len(new_nums)):
    dic[new_nums[i]]=i

#print(dic)
for i in nums:
    print(dic[i], end=' ')
