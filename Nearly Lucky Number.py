n=input()
a=0
for i in range(len(n)):
    if(n[i]=="4" or n[i]=="7"):
        a+=1
if(a==4 or a==7):
    print("YES")
else:
    print("NO")