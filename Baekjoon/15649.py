# 15649 N과 M(1)

n,m=map(int, input().split())

answer=[]

def f():
    if len(answer)==m:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            f()
            answer.pop()

f()

# import itertools

# n,m=map(int, input().split())
# nums=[i for i in range(1, n+1)]

# answer=itertools.permutations(nums, m)

# for i in answer:
#     for j in i:
#         print(j, end=' ')
#     print()
