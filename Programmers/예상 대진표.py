def solution(n,a,b):
    count=0
    first=max(a,b)
    second=min(a,b)
    while first!=second:
        count+=1
        if first%2==1:
            first=first+1
        if second%2==1:
            second=second+1
        first=first//2
        second=second//2
    return count
