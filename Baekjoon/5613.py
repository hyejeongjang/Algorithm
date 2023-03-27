# 5613 : 계산기 프로그램

result=[]
sign=[]
while True:
    tmp=input()
    if tmp=="=":
        break
    else:
        if tmp in "-*/+":
            sign.append(tmp)
        else:
            result.append(int(tmp))

answer=0
for i in range(len(sign)):
    a=result.pop(0)
    b=result.pop(0)

    if sign[i]=='+':
        answer=a+b
    elif sign[i]=='-':
        answer=a-b
    elif sign[i]=='*':
        answer=a*b
    else:
        answer=a//b
    result.insert(0, answer)
print(answer)
