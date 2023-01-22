n=int(input())
a=[]
for i in range(n):
    a.append(input())
    if(len(a[i])<=10):
        print(a[i])
    else:
        print(a[i][0]+str(len(a[i])-2)+a[i][len(a[i])-1])