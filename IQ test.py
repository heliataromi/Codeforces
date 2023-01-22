n=int(input())
a=list(map(lambda x: int(x),input().split()))
if(len(list(filter(lambda x: x%2==0,a)))==1):
    print(a.index(list(filter(lambda x: x%2==0,a))[0])+1)
else:
    print(a.index(list(filter(lambda x: x%2==1,a))[0])+1)