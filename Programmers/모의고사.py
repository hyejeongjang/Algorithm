def solution(answers):
    answer = []
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    thrid=[3,3,1,1,2,2,4,4,5,5]
    one=0
    two=0
    three=0
    li2=[]
    for i in range(len(answers)):
        if(answers[i]==first[i%5]):
            one=one+1
        if(answers[i]==second[i%8]):
            two=two+1
        if(answers[i]==thrid[i%10]):
            three=three+1
    li2.append(one)
    li2.append(two)
    li2.append(three)
    for i, score in enumerate(li2):
        if(max(li2)==score):
            answer.append(i+1)
    return answer 
