y=input()
a=int(y)+1
y=str(a)
while(y[0]==y[1] or y[1]==y[2] or y[2]==y[3] or y[0]==y[2] or y[0]==y[3] or y[1]==y[3]):
    a+=1
    y=str(a)
print(a)