# 2675 문자열 반복

t=int(input())
for _ in range(t):
    num, word=input().split()
    answer=''
    num=int(num)
    for i in word:
        answer+=i*num
    print(answer)
