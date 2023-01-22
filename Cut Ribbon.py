#incomplete
n, *p = map(int, input().split())
p = list(set(filter(lambda x: x != n, p)))
p.sort()
print(p)
ans = 0
num = 0
s = 0
for x in p:
    if(n%x == 0 and n//x > ans):
        ans = n//x
        break
if(ans == 0):
    for i in range(len(p)):
        num = n//p[i]
        s = num*p[i]
        while(s != n and s>0):
            s -= p[i]
            s += p[i+1] if i<len(p)-1 else p[-1]
        ans = num
print(ans)
