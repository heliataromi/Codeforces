a=input()
b=input()
c=input()
d=0
for x in c:
    if(c.count(x)!=a.count(x)+b.count(x)):
        d+=1
for x in a:
    if(a.count(x)+b.count(x)!=c.count(x)):
        d+=1
for x in b:
    if(a.count(x)+b.count(x)!=c.count(x)):
        d+=1
if(d==0):
    print("YES")
else:
    print("NO")