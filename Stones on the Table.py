n=int(input())
s=input()
a=0
for i in range(1,n):
    if(s[i-1]==s[i]):
        a+=1
print(a)