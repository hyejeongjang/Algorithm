def solution(k, tangerine):
    answer = 0
    dic={}
    
    for i in tangerine:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    
    #print(dic)
    new_dic=dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    #print(new_dic)
    
    count=0
    for i in new_dic:
        if k<=0:
            return answer
        k-=new_dic[i]
        answer+=1
            
    return answer
