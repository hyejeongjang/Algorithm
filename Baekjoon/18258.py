# 18258 큐2

from collections import deque
import sys

q=deque()
n=int(sys.stdin.readline())

for i in range(n):
    command=sys.stdin.readline().split()
    if command[0]=="push":
        q.append(command[1])
    elif command[0]=="pop":
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif command[0]=="size":
        print(len(q))
    elif command[0]=="empty":
        if q:
            print(0)
        else:
            print(1)
    elif command[0]=="front":
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
