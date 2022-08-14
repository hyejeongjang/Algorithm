# 10872 팩토리얼

def fac(x):
    if x>1:
        return x*fac(x-1)
    else:
        return 1

n=int(input())
print(fac(n))
