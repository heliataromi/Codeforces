a=input()
c=0
for i in range(len(a)):
    if(a[i] not in a[i+1:]):
        c+=1
if(c%2!=0):
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
