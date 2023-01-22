a=input()
b=""
c=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
d=["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z"]
for i in range(len(a)):
    if(a[i] not in "AaOoUuIiEeYy"):
        if(a[i] in c):
            b=b+"."+a[i]
        elif(a[i] in d):
            b=b+"."+c[d.index(a[i])]
print(b)