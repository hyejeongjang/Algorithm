# 10809 알파벳 찾기

word=input()
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alphabet: 
    print(word.find(i), end=' ')
