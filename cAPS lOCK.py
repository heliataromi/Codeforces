a=input()
if(a.isupper()):
    print(a.lower())
elif(a[0].islower() and a[1:].isupper()):
    print(a.swapcase())
elif(len(a)==1):
    print(a.upper())
else:
    print(a)