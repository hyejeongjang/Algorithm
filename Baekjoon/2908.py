# 2908 상수

a,b=input().split()
reversed_a=int(a[::-1])
reversed_b=int(b[::-1])

if reversed_a>reversed_b:
    print(reversed_a)
else:
    print(reversed_b)
