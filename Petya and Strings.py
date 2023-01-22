a=input()
b=input()
c=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
d=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
e=0
f=0
g=0
for i in range(len(a)):
    if(a[i] in c):
        f=c.index(a[i])
    elif(a[i] in d):
        f=d.index(a[i])
    if(b[i] in c):
        g=c.index(b[i])
    elif(b[i] in d):
        g=d.index(b[i])
    if(f==g):
        e+=0
    elif(f<g):
        if(e==0):
            e=-1
    elif(f>g):
        if(e==0):
            e=1
print(e)