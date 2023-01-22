#incompelete
import re
a=input()
b=input()
c=input()
d=0
if(re.search(b,a) and re.search(c,a)):
    if(c in a[re.search(b,a).end()-1:]):
        d+=1
if(re.search(b,a[::-1]) and re.search(c,a[::-1])):
    if(c in a[::-1][re.search(b,a).end()-1:]):
        d+=2
if(d==0):
    print("fantasy")
if(d==1):
    print("forward")
if(d==2):
    print("backward")
if(d==3):
    print("both")
