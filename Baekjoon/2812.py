# 2812 크게 만들기

import itertools

n,k=map(int, input().split())
num=list(input())
stack=[]

for number in num:
    while stack and stack[-1]<number and k>0:
        stack.pop()
        k-=1
    stack.append(number)

if k>0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
