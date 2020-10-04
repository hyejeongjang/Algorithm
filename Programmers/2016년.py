answer = ''
days=["THU", "FRI", "SAT","SUN", "MON", "TUE", "WED"] # 요일 : 1월 1일이 금요일이기 때문
day=[31,29,31,30,31,30,31,31,30,31,30,31]
count=0
for i in range(a): # 월
    if(a-1==i):
        count=count+b
    else:
        count=count+day[i]
count
days[(count)%7]
