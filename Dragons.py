s,n=map(lambda x:int(x),input().split())
a=''
c=[]
for i in range(n):
    b=list(map(lambda x:int(x),input().split()))
    c.append(b)
c.sort()
for i in range(n):
    if(s>c[i][0]):
        a="YES"
        s+=c[i][1]
    else:
        a="NO"
        break
print(a)