n, k = map(int, input().split())
c = 0
while(k <= 240 and c <= n):
    c += 1
    k += c * 5
print(c - 1)