# 4153 직각삼각형

while True:
    a,b,c=map(int, input().split())
    if a==0 and b==0 and c==0:
        exit()
    triangle=[a,b,c]
    triangle.sort()
    if (triangle[0]**2+triangle[1]**2==triangle[2]**2):
        print("right")
    else:
        print("wrong")

