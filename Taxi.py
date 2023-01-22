#incomplete
n=int(input())
s=input()
a=[]
b=n
for i in range(len(s)):
    if(s[i]!=" "):
        a.append(s[i])
for i in range(len(a)):
    for j in range(len(a)):
        if(int(a[i])+int(a[j])<=4 and i!=j):
            b-=1
            a.remove(a[j])
print(b)
