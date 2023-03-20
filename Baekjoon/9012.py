# 9012 : 괄호

import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
    tmp=list(input().strip())
    st=[]

    for i in tmp:
        if i=="(":
            st.append(i)
        else:
            if len(st)>0:
                st.pop()
            else:
                st.append(i)
                break

        #print(st)
    if len(st)==0:
        print("YES")
    else:
        print("NO")
