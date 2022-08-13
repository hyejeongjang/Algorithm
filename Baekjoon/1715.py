# 1715 카드 정렬하기

import heapq

n=int(input())
heap=[]
for _ in range(n):
    heap.append(int(input()))
heapq.heapify(heap)

answer=0
while len(heap)!=1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    result=a+b
    heapq.heappush(heap,result)
    answer+=result
print(answer)
