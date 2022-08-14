# 1931 회의실 배정

n=int(input())
meeting=[]
for _ in range(n):
    a,b=map(int, input().split())
    meeting.append([a,b])

meeting.sort(key=lambda x: (x[1], x[0]))

answer=0
# 끝나는 시간
endtime=0

for i in meeting:
    if endtime<i[0]:
        endtime=i[1]
        answer+=1

print(answer)
