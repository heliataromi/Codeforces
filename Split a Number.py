l=int(input())
n=input()
b=l//2
if(l>3):
    b-=1
d=10**100000
while(b<l):
    a=int(n[:b])
    c=int(n[b:])
    if(n[b:][0]!="0"):
        if(a+c<d):
            d=a+c
    b+=1
print(d)

