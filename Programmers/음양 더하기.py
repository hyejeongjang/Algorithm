def solution(absolutes, signs):
    ans=[]
    for index, value in enumerate(absolutes):
        # print(value)
        if signs[index]==False:
            value=value*(-1)
            ans.append(value)
        else:
            ans.append(value)
    return sum(ans)
