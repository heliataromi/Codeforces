ab=list(map(lambda x: int(x),input().split()))
c=0
while(ab[0]<=ab[1]):
    ab[0]*=3
    ab[1]*=2
    c+=1
print(c)