def solution(n, words):
    
    pre_char=words[0][-1]
    print(pre_char)
    for i in range(1, len(words)):
        print(pre_char)
        last_word=words[i][0]
        if last_word!=pre_char or words[i] in words[:i]:
            answer=[(i%n)+1, (i//n)+1]
            return answer
        pre_char=words[i][-1]
    else:
        answer=[0,0]
        return answer
                
