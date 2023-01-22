n=int(input())
groups=1
magnets=[]
for i in range(n):
    magnets.append(input())
for i in range(1,n):
    if(magnets[i]!=magnets[i-1]):
        groups+=1
print(groups)
