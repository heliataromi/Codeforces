n=input()
a=list(n)
if any([x!='4' and x!='7' for x in a]):
    if(int(n)%4==0 or int(n)%7==0):
        print("YES")
    else:
        print("NO")
else:
    print("YES")
