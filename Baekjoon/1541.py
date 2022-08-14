# 1541 잃어버린 괄호

equation=input().split('-')
answer=0

# 맨 앞에 더할 숫자들을 더해주자
plus_num=equation[0].split('+')
for i in plus_num:
    answer+=int(i)

# 더할 숫자들을 다 더해주고 뒤의 숫자들을 빼주자
for i in equation[1:]:
    for j in i.split('+'):
        answer-=int(j)

print(answer)
