nm=input().split()
for i in range(int(nm[0])):
    if(i%2==0):
        print(int(nm[1])*'#')
    if(i%4==1):
        print((int(nm[1])-1)*'.'+'#')
    if(i%4==3):
        print('#'+(int(nm[1])-1)*'.')