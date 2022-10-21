def solution(s):
    answer=""
    s=s.split(' ')
    for i in s:
        if i=="":
            answer+=" "
            continue

        tmp=""
        i=i.lower()
        if i[0].isdigit():
            answer+=i+" "
            continue
        else:
            tmp=i[0]
            tmp=tmp.upper()
            i=tmp+i[1:]
            answer+=i+" "
        
    return answer[:-1]
