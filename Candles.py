a=int(input())
b=int(input())
c=0
d=a
while(a>0):
    c=a//b
    d+=c
    a=c
print(d)
