n=int(input())
p=input().split()
q=input().split()
a=[]
b=0
for x in p[1:]:
    a.append(x)
for x in q[1:]:
    a.append(x)
for x in range(1,n+1):
    if(str(x) not in a):
        b+=1
if(b==0):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")