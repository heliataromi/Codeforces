nh=input().split()
a=input().split()
w=0
for i in range(int(nh[0])):
    if(int(a[i])>int(nh[1])):
        w+=2
    else:
        w+=1
print(w)