# 1436 영화감독 숌

import sys
input=sys.stdin.readline

n=int(input())
count=0
title=666
while True:
    if "666" in str(title):
        count+=1
        if count==n:
            print(title)
            break
    title+=1
