# 10815 숫자 카드
import sys
input=sys.stdin.readline

n=int(input())
num_n=set(map(int, input().split()))

m=int(input())
num_m=list(map(int, input().split()))

for i in num_m:
    if i in num_n:
        print(1, end=' ')
    else:
        print(0, end=' ')
