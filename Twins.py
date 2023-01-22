n=int(input())
a=input()
b=list(a)
for i in range(int(len(b)/2)):
    b.remove(" ")
c=0
for i in range(len(b)):
    c+=int(b[i])
b.sort()
b.reverse()
d=0
e=0
for i in range(len(b)):
    if(d<=c/2):
        d+=int(b[i])
        e+=1
print(e)
