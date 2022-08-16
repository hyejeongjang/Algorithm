# 11729 하노이의 탑 이동 순서

n=int(input())
count=0
def hanoi(n, start, to, end):
    if n==1:
        print(start, end)
    else:
        hanoi(n-1, start, end, to)
        print(start, end)
        hanoi(n-1, to, start, end)
# 총횟수
print(2**n-1)
hanoi(n,1,2,3)
