from collections import deque

def solution(s):
    
    temp=deque()
    for i in s:
        if len(temp)==0:
            temp.append(i)
        elif i==temp[-1]:
            temp.pop()
        else:
            temp.append(i)

    if len(temp)==0:
        return 1
    else:
        return 0
