a=input()
b=input()
c=''
for i in range(len(a)):
    c+='{0}'.format(0 if a[i]==b[i] else 1)
print(c)