# 10815 숫자 카드
import sys
input=sys.stdin.readline

n=int(input())
num_n=list(map(int, input().split()))
num_n.sort()

m=int(input())
num_m=list(map(int, input().split()))

# 이진 탐색
for i in num_m:
    start, end=0, n-1

    while True:
        mid=(start+end)//2
        if start>end:
            print(0, end=' ')
            break
        elif num_n[mid]>i:
            end=mid-1
        elif num_n[mid]<i:
            start=mid+1
        elif num_n[mid]==i:
            print(1, end=' ')
            break
