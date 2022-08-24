# 1316 그룹 단어 체커

n=int(input())
answer=n

for _ in range(n):
    word=input()
    for i in range(0, len(word)-1):
        if word[i]==word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            answer-=1
            break

print(answer)
