# 1026 보물

n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

a.sort() #a를 오름차순으로 정렬
answer=0
for i in range(len(a)):
    tmp=b.pop(b.index(max(b)))
    answer+=a[i]*tmp
print(answer)
