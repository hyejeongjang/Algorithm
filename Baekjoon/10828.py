# 10828 스택

import sys
n=int(sys.stdin.readline())

test_stack=[]

for i in range(n):
    com=sys.stdin.readline().split()
    
    if com[0]=="push":
        test_stack.append(com[1])
    elif com[0]=="pop":
        if len(test_stack)==0:
            print(-1)
        else:
            print(test_stack.pop())
    elif com[0]=="size":
        print(len(test_stack))
    elif com[0]=="empty":
        if len(test_stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(test_stack)==0:
            print(-1)
        else:
            print(test_stack[-1])
