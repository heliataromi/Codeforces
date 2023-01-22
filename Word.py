import string
s=input()
up=0
low=0
for i in s:
    if(i in string.ascii_lowercase):
        low+=1
    if(i in string.ascii_uppercase):
        up+=1
if(up>low):
    print(s.upper())
else:
    print(s.lower())