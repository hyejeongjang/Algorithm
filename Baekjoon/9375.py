# 9375 패션왕 신해빈

t=int(input())
for _ in range(t):
    # 가지고 있는 의상의 수
    n=int(input())
    outfits={}
    answer=[]
    for _ in range(n):
        a,b=map(str, input().split())
        if b in outfits:
            outfits[b]+=1
        else:
            outfits[b]=1
    answer=list(outfits.values())
    print_answer=1
    for i in answer:
        print_answer=print_answer*(i+1)
    print(print_answer-1)
