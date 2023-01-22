s=input()
a=list(s)
for i in range(int((len(a)-1)/2)):
    a.remove("+")
a.sort()
b=""
for i in range(len(a)):
    if(i!=len(a)-1):
        b=b+a[i]+"+"
    elif(i==len(a)-1):
        b=b+a[i]
print(b)
