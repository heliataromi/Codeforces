n=int(input())
a=""
for i in range(n):
    if(i%2==0):
        a+="I hate "
    else:
        a+="I love "
    if(i==n-1):
        a+="it"
    else:
        a+="that "
print(a)