import string
n=int(input())
s=input()
a=0
for x in string.ascii_lowercase:
    if(x not in s.lower()):
        a+=1
if(a!=0):
    print("NO")
else:
    print("YES")