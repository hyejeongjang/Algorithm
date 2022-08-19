# 1157 단어 공부

word=input().upper()
dic={}
for i in word:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
# print(dic)
dic_max=max(dic.values())

count=0
for key, value in dic.items():
    if dic_max==value:
        count+=1
    else:
        count=count
if count!=1:
    print("?")
else:
    print(max(dic, key=dic.get))
