# #  1920 수 찾기

from operator import truediv
import sys

n=int(sys.stdin.readline())
#list_n=set(map(int, sys.stdin.readline().split()))
list_n=list(map(int, input().split()))

m=int(sys.stdin.readline())
list_m=list(map(int, sys.stdin.readline().split()))

# set 이용
# for i in list_m:
#     if i in list_n:
#         print(1)
#     else:
#         print(0)

# 이분탐색 이용
list_n.sort()

def binary(target):
    left=0
    right=len(list_n)-1
    while left<=right:
        mid=(left+right)//2
        if list_n[mid]==target:
            return True
        elif list_n[mid]>target:
            right=mid-1
        else:
            left=mid+1

for i in range(m):
    if binary(list_m[i]):
        print(1)
    else:
        print(0)
