t = int(input())

for k in range(t):
    n = int(input())
    balls = list(map(int, input().split()))
    print(balls.index(max(balls)) + 1)
