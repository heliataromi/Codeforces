n=int(input())
a=0
for i in range(n):
    pq=input().split()
    if(int(pq[1])-int(pq[0])>=2):
        a+=1
print(a)