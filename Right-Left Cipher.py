#incompelete
t=list(input())
s=''
a=len(t)
#if(a%2!=0):
    #s+=t[len(t)//2]
    #t.pop(len(t)//2)
while(len(t)!=0):
    if(len(t)%2==0):
        s+=t[len(t)//2-1]
        t.pop(len(t)//2-1)
    if(len(t)%2!=0):
        s+=t[len(t)//2]
        t.pop(len(t)//2)
        #if(len(t)!=0):
            #s+=t[len(t)//2]
            #t.pop(len(t)//2)
print(s)
