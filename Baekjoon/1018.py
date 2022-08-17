# 1018 체스판 다시 칠하기

import sys
input=sys.stdin.readline

n,m=map(int, input().split())
board=[]
answer=[]

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        numw=0
        numb=0
        for a in range(i, i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if board[a][b]!='W':
                        numw+=1
                    if board[a][b]!='B':
                        numb+=1
                else:
                    if board[a][b]!='W':
                        numb+=1
                    if board[a][b]!='B':
                        numw+=1

        answer.append(numw)
        answer.append(numb)

print(min(answer))
