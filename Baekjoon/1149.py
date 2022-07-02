  # 1149 RGB거리

# 집의 수
n=int(input())
prices=[]
for _ in range(n):
    prices.append(list(map(int, input().split())))

for i in range(1, n):
    prices[i][0]=prices[i][0]+min(prices[i-1][1], prices[i-1][2])
    prices[i][1]=prices[i][1]+min(prices[i-1][0], prices[i-1][2])
    prices[i][2]=prices[i][2]+min(prices[i-1][1], prices[i-1][0])

print(min(prices[-1]))
